from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Post
import datetime

# Create your views here.

def index(request):
    allposts = Post.objects.all()
    return render(request, 'tidder/index.html', {'allposts': allposts})

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

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
        else:
            print('\nform is invalid\n')
    else:
        form = PostForm()
    return render(request, 'tidder/post_form.html', {'form': form})

def post_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'tidder/post_view.html', {'post': post})
