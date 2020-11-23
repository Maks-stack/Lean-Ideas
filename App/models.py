from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

User._meta.get_field('username')._unique = True
User._meta.get_field('email')._unique = True

class Idea(models.Model):
    CATEGORY_CHOICE = [('TECH','Technology')]
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE)
    lastUpdate = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now_add=True)





