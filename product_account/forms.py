from django import forms
from product_account.models import Product_account

class Product_accountForm(forms.ModelForm):
    class Meta:
        model = Product_account
        fields = ['title', 'price', 'image', 'description', 'available']
