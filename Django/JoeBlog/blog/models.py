from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BlogColumn(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    date = models.DateField(auto_now=True)


class Blog(models.Model):
    column_id = models.ForeignKey(BlogColumn)
    title = models.CharField(max_length=20, null=False)
    author = models.CharField(max_length=20, null=True)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    tags = models.TextField()


class Comment(models.Model):
    name = models.CharField(max_length=20, null=False)
    message = models.TextField(null=False)
    date = models.DateField(auto_now=True)
