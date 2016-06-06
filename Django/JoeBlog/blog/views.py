from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext


def index(request):
    context = {"checkItem": 4, "title": "关于"}
    return render_to_response('about.html', context, context_instance=RequestContext(request))


def comment(request):
    context = {"checkItem": 3, "title": "留言"}
    return render_to_response('comments.html', context, context_instance=RequestContext(request))


def blog(request):
    return render_to_response('blogs.html', {"checkItem": 2, "title": "博客"}, context_instance=RequestContext(request))
