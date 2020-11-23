from django.urls import path, re_path
from App.views import register
from django.contrib import admin

import re

from django.contrib.auth.views import LoginView, LogoutView

from . import views

from App.views import register, getIdeas, addIdea, ideaDetailView

from django.http import HttpResponse

urlpatterns = [

    path('admin/', admin.site.urls),
    #path('',index, name='index'),
    path('register', register, name='register'),
    path("", LoginView.as_view(template_name="index.html", redirect_authenticated_user=True),name="login"),
    path("logout", LogoutView.as_view(),name ="logout"),
    path("ideaBoard", getIdeas, name="ideaBoard"),
    path("addIdea", addIdea, name="addIdea"),
    re_path(r"^ideaDetails/\d", ideaDetailView)
] 