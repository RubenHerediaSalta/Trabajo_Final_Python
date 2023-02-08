from django.db import models

class Product_account(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='account_images', null=True, blank=True)
    description = models.CharField(max_length=500)
