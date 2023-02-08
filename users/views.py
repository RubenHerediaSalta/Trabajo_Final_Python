from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from users.models import *
from users.forms import *

def not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(not_logged_in, login_url='/users/profile-detail')
def login_view(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile_detail')

        form = AuthenticationForm()
        context ={
            'form':form,
            'errors':'Usuario o contraseña incorrectos!'
        }
        return render(request, 'users/login.html', context=context)

@user_passes_test(not_logged_in, login_url='/users/profile-detail')
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context ={
            'form':form
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user) #para crear el perfil vacio del usuario
            return redirect('login')

        context = {
            'errors': form.errors,
            'form':RegisterForm()
        }

        return render(request, 'users/register.html', context=context)

@login_required
def update_user_profile(request):
    user = request.user
    if request.method == 'GET':
        form = UserProfileForm(initial={
            'first_name': request.user.profile.first_name,
            'last_name': request.user.profile.last_name,
            'phone':request.user.profile.phone,
            'profile_picture':request.user.profile.profile_picture
        })
        context ={
            'form':form
        }
        return render(request, 'users/update_profile.html', context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.profile_picture = form.cleaned_data.get('profile_picture')
            user.profile.save()
            return redirect('index')
        
        context = {
            'errors':form.errors,
            'form':UserProfileForm()
        }
        return render(request, 'users/register.html', context=context)

@login_required
def profile_detail(request):
    return render(request, 'users/profile_detail.html')