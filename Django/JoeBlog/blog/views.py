from django import forms
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render

# Create your views here.
from django.template import RequestContext

from blog.forms import LoginForm


def login(request):
    if request.method == 'GET':
        return render(request, 'ad/login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponse('success')
            else:
                return HttpResponse('password is wrong')
        else:
            return HttpResponse('user does not exist')


def logout(request):
    auth.logout(request)
    return HttpResponse('已经注销')


@login_required
def admin(request):
    return render(request, 'ad/admin.html')


@login_required
def adblogs(request):
    return render(request, 'ad/blogs.html')


def index(request):
    context = {"checkItem": 4, "title": "关于"}
    return render_to_response('about.html', context, context_instance=RequestContext(request))


def comment(request):
    context = {"checkItem": 3, "title": "留言"}
    comments = [{"name": "user1", "message": "message1", "date": "2016-6-5"},
                {"name": "user2", "message": "message2", "date": "2016-6-6"}]
    context["comments"] = comments
    context["pages"] = range(5)
    context["nowpage"] = 0
    return render_to_response('comments.html', context, context_instance=RequestContext(request))


def blog(request):
    context = {"checkItem": 2, "title": "博客"}
    blogsCategory = [{"id": 1, "name": "栏目1"}, {"id": 2, "name": "栏目2"}]
    blogs = [{"title": "title1"}, {"title": "title2"}, {"title": "title3"}]
    context["category"] = blogsCategory
    context["blogs"] = blogs
    return render_to_response('blogs.html', context, context_instance=RequestContext(request))
