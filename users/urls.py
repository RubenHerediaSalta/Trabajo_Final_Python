from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import *


urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page= 'index')),
    path('signup/', register, name = 'register'),
    path('update/profile/', update_user_profile, name = 'update_user_profile'),
    path('profile-detail/', profile_detail, name = 'profile_detail'),
]