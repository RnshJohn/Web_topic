
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .form import RegisterForm, LoginForm, ProfileForm, PwdChangeForm
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib import messages
from django.contrib.auth.models import Group
def homepage(request):
    print("Homepage")
    return HttpResponse("index ok")


@login_required(login_url='login')
@allowed_users(allowed_roles=['profile'])
def userPage(request):
    customer = request.user.profile
    user = User(instance=customer)
    user_profile = get_object_or_404(UserProfile, user=user)
    return render(request, 'main/Home.html', {'user': user, 'image': user_profile})


@login_required(login_url='login')
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

            return HttpResponseRedirect(reverse('main:room', args=[user.id]))


    else:
        default_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user_profile.phone_number,
        }
        form = ProfileForm(default_data)
    return render(request, 'main/profile_updata.html', {'form': form, 'user': user})

@unauthenticated_user
def register(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            phone_number = form.cleaned_data['phone_number']
            image = form.cleaned_data['image']
            user = User.objects.create_user(username=username, password=password, email=email)

            user_profile = UserProfile(user=user, phone_number=phone_number, image=image)

            user_profile.save()

            return HttpResponseRedirect("/account/login")
    else:
        form = RegisterForm()
    return render(request, 'main/registration.html', {'form': form})

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:user-page'))
            else:
                # 登入失敗
                messages.info(request, "Username OR password is incorrect")
                # return render(request, 'main/login.html', {'form': form, "message": "Wrong password Please Try again"})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login")


@login_required()
def pwd_change(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = PwdChangeForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data['old_password']
            username = user.username

            user = auth.authenticate(username=username, password=password)

            if user is not None and user.is_activate:
                new_password = form.cleaned_data['password2']
                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect('/account/login/')

            else:
                return render(request, 'main/pwd_change.html',
                              {'form': form, 'user': user, 'message': 'Old password is wrong Try again'})

    else:
        form = PwdChangeForm()

    return render(request, 'main/pwd_change.html', {'form': form, 'user': user})




