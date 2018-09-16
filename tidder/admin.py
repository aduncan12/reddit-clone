from django.contrib import admin
from .models import User, UserProfile, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)