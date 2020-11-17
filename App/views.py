from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

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
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username, email, password)
                user.first_name = fname
                user.last_name = lname
                user.save()
                return redirect('login')
    else:
        return render(request, 'register.html')