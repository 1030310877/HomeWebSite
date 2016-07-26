from django.test import TestCase

# Create your tests here.
from blog.models import BlogColumn

BlogColumn.objects.create(name="test", date="2015-07-11")
