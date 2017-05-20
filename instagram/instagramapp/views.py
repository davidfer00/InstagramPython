from django.shortcuts import render

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
    print (request.POST[ 'Email' ])
    print (request.POST[ 'Name' ])
    print (request.POST[ 'Username' ])
    print (request.POST[ 'Password' ])
    return render(request, 'index.html')
