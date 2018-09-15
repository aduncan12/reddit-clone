from django.contrib import admin
from .models import UniqueUser, UserProfile

# Register your models here.
admin.site.register(UniqueUser)
admin.site.register(UserProfile)