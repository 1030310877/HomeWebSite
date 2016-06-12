from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext


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
