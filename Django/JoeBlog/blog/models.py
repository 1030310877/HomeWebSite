from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class BlogColumn(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    date = models.DateField()


class Blog(models.Model):
    column_id = models.ForeignKey(BlogColumn)
    title = models.CharField(max_length=20, null=False)
    author = models.CharField(max_length=20, null=True)
    content = models.TextField()
    date = models.DateField()
    tags = models.TextField()
