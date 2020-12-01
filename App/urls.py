from django.urls import path, re_path
from App.views import register, editIdea, deleteIdea
from django.contrib import admin

import re

from django.contrib.auth.views import LoginView, LogoutView

from . import views

from App.views import register, getIdeas, addIdea, getIdeaDetail, redirectIdeaBoard, voteIdea

from django.http import HttpResponse

urlpatterns = [

    path('admin/', admin.site.urls),
    #path('',index, name='index'),
    path('register', register, name='register'),
    path("", LoginView.as_view(template_name="index.html", redirect_authenticated_user=True),name="login"),
    path("logout", LogoutView.as_view(),name ="logout"),
    path("ideaBoard/<str:filter>", getIdeas, name="ideaBoard"),
    path("ideaBoard", redirectIdeaBoard),
    path("addIdea", addIdea, name="addIdea"),
    path("ideaDetails/<int:ideaID>", getIdeaDetail, name="ideaDetails"),
    path("editIdea/<int:ideaID>", editIdea, name="editIdea"),
    path("deleteIdea/<int:ideaID>", deleteIdea, name="deleteIdea"),
    path("voteIdea/", voteIdea)
    
] 