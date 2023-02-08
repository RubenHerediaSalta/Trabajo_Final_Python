from django.contrib import admin
from product_coaching.models import Product_coaching

@admin.register(Product_coaching)
class Product_coachingAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image', 'description', 'available')