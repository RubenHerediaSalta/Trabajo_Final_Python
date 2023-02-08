from django.contrib import admin
from users.models import UserProfile
from .models import *


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','first_name', 'last_name','phone', 'profile_picture')

