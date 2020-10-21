from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


def login(request):
    return render(request, 'user/login.html')

def


def register(request):
    if request.method == 'POST':
        form

def