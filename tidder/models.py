from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

        
# class UniqueUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=20, default=None)
#     signed_up = models.DateTimeField(auto_now_add=True)
#     is_staff = False

#     def __str__(self):
#         return self.user.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200, blank=True)
    site_url = models.URLField(blank=True) 
    content = models.TextField(blank=True)
    picture = models.ImageField(upload_to='post_pics',blank=True)
    post_time = models.DateTimeField(auto_now_add=True)
    post_vote = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class PostSave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save_time = models.DateTimeField(auto_now_add=True)

class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    comment_vote = models.IntegerField()

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    # posts = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    # comments = models.ForeignKey(CommentPost, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    portfolio = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_staff=True

    def __str__(self):
        return self.user.username
        