from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from App.models import Idea, Comment, VoteUser
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

def checkValidity(fname, lname, username, password):
    error_message = None
    if not fname.isalpha():
        error_message = "Your first name should contain only letters."
    elif not lname.isalpha():
        error_message = "Your last name should contain only letters."
    elif not username.isalnum():
        error_message = "Your username should only contain letters and numbers."
    elif not password.isalnum():
        error_message = "Your password should only contain letters and numbers."
    return error_message

def login(request):
    if request.user.is_authenticated():
       return redirect('ideaBoard')

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

            error_message = checkValidity(fname,lname,username,password)
            if error_message:
                messages.error(request, error_message)
                return render(request, "register.html")
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

@login_required
def addIdea(request):
    if request.method == "POST":
        if request.POST.get('name') and \
            request.POST.get('content') and \
            request.POST.get('category'):

            name = request.POST['name']
            content =request.POST['content']
            category = request.POST['category']
            author = request.user
            vote = 0

            idea = Idea(name=name, content=content, category=category, author=author,
                        vote=vote)
            idea.save()
            return redirect('/ideaBoard/own')

    else:
        return render(request, "addIdea.html")

@login_required
def editIdea(request, ideaID):
    idea = Idea.objects.get(id=ideaID)
    if request.method == "POST":
        if request.POST.get('name') and \
            request.POST.get('content') and \
            request.POST.get('category'):

            name = request.POST['name']
            content =request.POST['content']
            category = request.POST['category']
            idea.name = name
            idea.category = category
            idea.content = content
            idea.save()
            return redirect('/ideaBoard/own')

    else:
        return render(request, "editIdea.html", {'idea':idea})

@login_required
def deleteIdea(request, ideaID):
    idea = Idea.objects.get(id=ideaID)
    idea.delete()
    return redirect('/ideaBoard/own')

@login_required
def getIdeas(request, filter):
    ideas = Idea.objects.all()
    votedIdeas = VoteUser.objects.filter(votingUser = request.user).values_list('votingIdea', flat=True)
    list = []
    i = 0
    for index in votedIdeas:
        list.append(votedIdeas[i])
        i = i + 1
    print(votedIdeas)
    print(ideas)
    if filter == "own":
        ideas = Idea.objects.filter(author=request.user)
    
    return render(request,'ideaBoard.html', {'ideas': ideas, 'list': list})

@login_required
def redirectIdeaBoard(request):
    return redirect('ideaBoard/own')

@login_required
def getIdeaDetail(request, ideaID):
    idea = Idea.objects.get(id=ideaID)
    if idea:
        comments = Comment.objects.filter(idea=idea)
        if request.method == "POST":
            if request.POST.get('content'):
                content = request.POST['content']
                author = request.user
                comment_idea = idea

                comment = Comment(content=content,author=author, idea=comment_idea)
                comment.save()
                return render(request, 'ideaDetails.html', {'idea':idea, 'comments':comments})
        else:
            return render(request,'ideaDetails.html', {'idea':idea, 'comments':comments})

@login_required
def voteIdea(request):    
    ideaID = request.POST['ideaID']

    idea = Idea.objects.get(id=ideaID)
    votings = VoteUser.objects.filter(votingIdea=idea, votingUser=request.user)
    if not votings:
        idea.vote += 1
        idea.save()

        new_vote = VoteUser(votingIdea=idea, votingUser=request.user)
        new_vote.save()

    if request.method == "POST":
        content = {"votes": idea.vote}
        return JsonResponse(content)
    
@login_required
def listUserIdeas(request):
    if request.method == "POST":
        error = 'User does not exist'
        user = User.objects.filter(username = request.POST['user'])
        if user:
            ideas = Idea.objects.filter(author = user[0])
            return render(request, "ideaBoard.html", {'ideas':ideas})
        else:
            return render(request, "ideaBoard.html", {'error':error})
    else:
        return render(request, 'ideaBoard.html')    
       
