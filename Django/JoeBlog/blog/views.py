from datetime import date

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, render

# Create your views here.
from blog.forms import LoginForm, RenameColumnForm, DeleteBlogForm, DeleteColumnForm, AddColumnForm, SaveBlogForm
from blog.models import BlogColumn, Blog, Comment


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
    all_column = BlogColumn.objects.all()
    for column in all_column:
        column_model = {"column_name": column.name, "column_id": column.id}
        blogs_with_column = Blog.objects.filter(column_id=column.id)
        column_model["blogs"] = blogs_with_column
        context["data"].append(column_model)
    return render_to_response('ad/blogs.html', context)


def delete_blog(request):
    if request.is_ajax() and request.method == 'POST':
        form = DeleteBlogForm(request.POST)
        if form.is_valid():
            blog_id = form.cleaned_data['blogId']
            try:
                item = Blog.objects.get(id=blog_id)
            except Exception as error:
                item = None
            if item is not None:
                item.delete()
                return HttpResponse("success")
            else:
                return HttpResponse("failed, blog does not exist")


@login_required
def edit_blog(request):
    if request.method == 'GET':
        context = {}
        type = request.GET.get('type')
        context['type'] = type
        column_id = request.GET.get('column_id')
        context['column_id'] = int(column_id)
        columns = BlogColumn.objects.all()
        context['columns'] = columns
        blog_id = request.GET.get('blog_id')
        if blog_id is not None:
            context['blog_id'] = int(blog_id)
            blog_title = Blog.objects.get(id=blog_id).title
            context['blog_title'] = blog_title
            blog_content = Blog.objects.get(id=blog_id).content
            context['blog_content'] = blog_content
        return render_to_response('ad/blog_edit.html', context)


def save_blog(request):
    if request.is_ajax() and request.method == 'POST':
        form = SaveBlogForm(request.POST)
        if form.is_valid():
            column_id = form.cleaned_data['column_id']
            blog_id = form.cleaned_data['blog_id']
            blog_title = form.cleaned_data['blog_title']
            blog_content = form.cleaned_data['blog_content']
            try:
                blog = Blog.objects.get(id=blog_id)
            except Exception as error:
                blog = None
            if blog is not None:
                blog.title = blog_title
                blog.column_id = BlogColumn.objects.get(id=column_id)
                blog.content = blog_content
                blog.date = date.today()
                blog.save()
            else:
                column = BlogColumn.objects.get(id=column_id)
                Blog.objects.create(title=blog_title, column_id=column, content=blog_content)
            return HttpResponse("success")
        else:
            return HttpResponse("data is invalid")
    return HttpResponse("not support request method")


def add_column(request):
    if request.is_ajax() and request.method == 'POST':
        form = AddColumnForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            BlogColumn.objects.create(name=name)
            return HttpResponse("success")


def rename_column(request):
    if request.is_ajax() and request.method == 'POST':
        form = RenameColumnForm(request.POST)
        if form.is_valid():
            column_id = form.cleaned_data['columnId']
            new_name = form.cleaned_data['newName']
            try:
                item = BlogColumn.objects.get(id=column_id)
            except Exception as error:
                item = None
            if item is not None:
                item.name = new_name
                item.save()
                return HttpResponse("success")
            else:
                return HttpResponse("the column does not exist")
        else:
            return HttpResponse("data is not complete")


def delete_column(request):
    if request.is_ajax() and request.method == 'POST':
        form = DeleteColumnForm(request.POST)
        if form.is_valid():
            column_id = form.cleaned_data['columnId']
            try:
                item = BlogColumn.objects.get(id=column_id)
            except Exception:
                item = None
            if item is not None:
                item.delete()
                return HttpResponse("success")
            else:
                return HttpResponse("failed, blog does not exist")


def index(request):
    context = {"checkItem": 3, "title": "关于"}
    return render_to_response('about.html', context)


def comment(request):
    context = {"checkItem": 2, "title": "留言"}
    page = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 10)
    all_page = Comment.objects.all().count()
    comments = Comment.objects.order_by(date)[(page - 1) * per_page:page * per_page]
    context["comments"] = comments
    context["pages"] = all_page
    context["nowpage"] = page
    return render_to_response('comments.html', context)


def blog(request):
    context = {"checkItem": 1, "title": "博客"}
    columns = BlogColumn.objects.all()
    blogs = Blog.objects.all()
    context['columns'] = columns
    context['blogs'] = blogs
    return render_to_response('blogs.html', context)


def get_blog(request):
    blog_id = request.GET.get('blog_id')
    blog = Blog.objects.get(id=blog_id)
    return HttpResponse(blog.content)
