from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')
def user(request):
    return render(request, 'user.html')

def create_user (request):
    _email = request.POST[ 'email' ]
    _username = request.POST[ 'username' ]
    _name = request.POST[ 'name' ]
    _password = request.POST[ 'password' ]
    print (_email)
    print (_name)
    print (_username)
    print (_password)
    user=User.objects.create_user( username = _username, email = _email, first_name = _name, password=_password)
    myUser = MiUsuario( usuario = user )
    myUser.save()
    print (user)
    print (user.password)
    return redirect('login')
