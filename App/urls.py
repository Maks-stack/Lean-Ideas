from django.urls import path
from App.views import register, index
from django.contrib import admin

from django.contrib.auth.views import LoginView, LogoutView

from . import views

from App.views import register

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('register', register, name='register'),
    path("login", LoginView.as_view(template_name="login.html"),name="login"),
    path("logout", LogoutView.as_view(),name ="logout")
] 