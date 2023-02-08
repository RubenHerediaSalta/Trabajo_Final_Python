from django.db import models

class Product_coaching(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='coaching_images', null=True, blank=True)
    description = models.CharField(max_length=500)
    available = models.BooleanField(default=True)
