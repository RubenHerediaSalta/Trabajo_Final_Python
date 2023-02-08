from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from coaches.models import Coaches


def user_is_admin(user):
    return user.is_staff

def index(request):
    images = Coaches.objects.all()
    return render(request, 'index.html', {'images':images})

def about(request):
    return render(request, 'about.html')

@user_passes_test(user_is_admin)
def controlpanel(request):
    return render(request, 'controlpanel.html')
