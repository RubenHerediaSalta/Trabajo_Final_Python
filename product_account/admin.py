from django.contrib import admin
from product_account.models import Product_account

@admin.register(Product_account)
class Product_accountAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description')