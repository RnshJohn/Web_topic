from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .form import RegisterForm, LoginForm, ProfileForm, PwdChangeForm
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.



def login(request):
    return render(request, 'main/login.html')

def profile(request, pk)
    user = get_object_or_404(User, pk=pk)
    return render(request, 'main/profile.html')

def profile_updata

def register(request):
    if request.method == 'POST':
        form

def