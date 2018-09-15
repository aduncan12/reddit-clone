from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Post

# Create your views here.

def index(request):
    return render(request,'tidder/index.html')

@login_required
def special(request):
    return HttpResponse("Welcome to tiddeR!")

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    registered = False
    # if we are trying to create a user, not get a new user view
    if request.method == 'POST':
        # we are populating a Form object with data from our request body (username, email, password)
        user_form = UserForm(data=request.POST)
        # we are populating a Form object with data from our request body (profile_pic, portfolio_site)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return redirect('index')

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'tidder/register.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account is inactive")

        else:
            print("Someone tried to login and failed")
            # print(f'They used username: {username} and password: {password}')
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'tidder/login.html', {})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            site_url = form.cleaned_data.get('site_url')
            post = Post(title=title, content=content, site_url=site_url, user=request.user)
            print(post)
            post.save()
            return redirect('index', pk=post.pk)
        else:
            print('\nform is invalid\n')
    else:
        form = PostForm()
    return render(request, 'tidder/post_form.html', {'form': form})