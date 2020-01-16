from django.db import models

# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    message = models.CharField(max_length=500,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    source = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    urltoimage = models.CharField(max_length=50)
    published = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
