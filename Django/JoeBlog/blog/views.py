from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

# Create your views here.
from blog.forms import LoginForm, RenameColumnForm, DeleteBlogForm, DeleteColumnForm, AddColumnForm
from blog.models import BlogColumn, Blog


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
    context = {"data": []}
    allColumn = BlogColumn.objects.all()
    for column in allColumn:
        columnModel = {}
        columnModel["column_name"] = column.name
        columnModel["column_id"] = column.id
        blogsWithColumn = Blog.objects.filter(column_id=column.id)
        columnModel["blogs"] = blogsWithColumn
        context["data"].append(columnModel)
    return render_to_response('ad/blogs.html', context)


def deleteBlog(request):
    if request.is_ajax() and request.method == 'POST':
        form = DeleteBlogForm(request.POST)
        if form.is_valid():
            blogId = form.cleaned_data['blogId']
            try:
                item = Blog.objects.get(id=blogId)
            except Exception as error:
                item = None
            if item is not None:
                item.delete()
                return HttpResponse("success")
            else:
                return HttpResponse("failed, blog does not exist")


def editBlog(request):
    if request.method == 'GET':
        return render(request, 'ad/blog_edit.html')


def addColumn(request):
    if request.is_ajax() and request.method == 'POST':
        form = AddColumnForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            BlogColumn.objects.create(name=name)
            return HttpResponse("success")


def renameColumn(request):
    if request.is_ajax() and request.method == 'POST':
        form = RenameColumnForm(request.POST)
        if form.is_valid():
            columnId = form.cleaned_data['columnId']
            newName = form.cleaned_data['newName']
            try:
                item = BlogColumn.objects.get(id=columnId)
            except Exception as error:
                item = None
            if item is not None:
                item.name = newName
                item.save()
                return HttpResponse("success")
            else:
                return HttpResponse("the column does not exist")
        else:
            return HttpResponse("data is not complete")


def deleteColumn(request):
    if request.is_ajax() and request.method == 'POST':
        form = DeleteColumnForm(request.POST)
        if form.is_valid():
            columnId = form.cleaned_data['columnId']
            try:
                item = BlogColumn.objects.get(id=columnId)
            except Exception:
                item = None
            if item is not None:
                item.delete()
                return HttpResponse("success")
            else:
                return HttpResponse("failed, blog does not exist")


def index(request):
    context = {"checkItem": 4, "title": "关于"}
    return render_to_response('about.html', context)


def comment(request):
    context = {"checkItem": 3, "title": "留言"}
    comments = [{"name": "user1", "message": "message1", "date": "2016-6-5"},
                {"name": "user2", "message": "message2", "date": "2016-6-6"}]
    context["comments"] = comments
    context["pages"] = range(5)
    context["nowpage"] = 0
    return render_to_response('comments.html', context)


def blog(request):
    context = {"checkItem": 2, "title": "博客"}
    blogsCategory = [{"id": 1, "name": "栏目1"}, {"id": 2, "name": "栏目2"}]
    blogs = [{"title": "title1"}, {"title": "title2"}, {"title": "title3"}]
    context["category"] = blogsCategory
    context["blogs"] = blogs
    return render_to_response('blogs.html', context)
