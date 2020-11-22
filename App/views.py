from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.models import Idea

from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.user.is_authenticated():
       return redirect('ideaBoard')

@login_required
def getIdeas(request):
    print("INDEX")
    ideas = Idea.objects.all
    return render(request,'ideaBoard.html', {'ideas': ideas})

def register(request):
    if request.method == 'POST':
        if request.POST.get('fname') and \
                request.POST.get('lname') and \
                request.POST.get('psw') and \
                request.POST.get('email') and \
                request.POST.get('psw-repeat'):

            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['psw']
            passwordCheck = request.POST['psw-repeat']
            if password != passwordCheck:
                messages.error(request, 'Your passwords do not match.')
                return render(request, 'register.html')
            else:
                users = User.objects.filter(username=username)
                if users:
                    messages.error(request, 'The username already exists.')
                    return render(request, 'register.html')
                users = User.objects.filter(email=email)
                if users:
                    messages.error(request, 'The email address already exists.')
                    return render(request, 'register.html')
                user = User.objects.create_user(username, email, password)
                user.first_name = fname
                user.last_name = lname
                user.save()
                return redirect('login')
    else:
        return render(request, 'register.html')
       