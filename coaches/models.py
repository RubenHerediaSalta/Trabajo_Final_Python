from django.db import models

class Coaches(models.Model):
    name = models.ImageField(upload_to='coaches_images', null=True, blank=True)
    background = models.ImageField(upload_to='coaches_images', null=True, blank=True)
    imagepop = models.ImageField(upload_to='coaches_images', null=True, blank=True)
    