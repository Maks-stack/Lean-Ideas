from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Idea(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.IntegerField()

class Comment(models.Model):
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)




