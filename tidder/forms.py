from django import forms
from .models import User, UserProfile, Post

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta():
        model = UserProfile
        fields = ('portfolio_site','profile_pic')

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'site_url', 'content', 'picture')