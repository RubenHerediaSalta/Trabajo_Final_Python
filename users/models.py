from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, null=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, null=True, verbose_name='Apellido')
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Telefono')
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True, verbose_name='Imagen de perfil')