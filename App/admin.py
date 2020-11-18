from django.contrib import admin


# Register your models here.

from .models import Idea, Comment

admin.site.register(Idea)
admin.site.register(Comment)
