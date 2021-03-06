"""JoeBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^index', views.index),
    url(r'^about', views.index),
    url(r'^comment', views.comment),
    url(r'^blogs$', views.blog),
    url(r'^blogs/getblog$', views.get_blog),
    url(r'^login', views.login),
    url(r'^logout$', views.logout),
    url(r'^ad/admin$', views.admin),
    url(r'^ad/blogs$', views.adblogs),
    url(r'^ad/blogs/addColumn$', views.add_column),
    url(r'^ad/blogs/deleteColumn$', views.delete_column),
    url(r'^ad/blogs/renameColumn$', views.rename_column),
    url(r'^ad/blogs/editBlog$', views.edit_blog),
    url(r'^ad/blogs/deleteBlog$', views.delete_blog),
    url(r'^ad/blogs/save$', views.save_blog)
]
