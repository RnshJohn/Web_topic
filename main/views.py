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

def profile_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            user.first_name = form.clean_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.phone_number = form.cleaned_data['phone_number']
            user_profile.save()

            return HttpResponseRedirect(reverse('main:profile', args=[user.id]))


        else:
            default_data = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number': user_profile.phone_number,
            }
            form = ProfileForm(default_data)
            return render(request, 'main/profile_updata.html')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            user = User.objects.create_user(username=username, password=password, email=email)

            user_profile = UserProfile(user=user)
            user_profile.save()

def