from django.urls import path
from django.contrib import admin

from App.views import register

urlpatterns = [

    path('admin/', admin.site.urls),
    path('register', register, name='register')
] 