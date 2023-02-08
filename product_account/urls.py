from django.urls import path
from product_account.views import *


urlpatterns = [
    path('controlpanel-product_account/', controlpanel, name='controlpanel_product_account'),
    path('create-product_account/', Product_accountCreateView.as_view(), name='add_product_account'),
    path('list-product_account', list_product_account, name='list_product_account'),
    path('update-product_account/<int:pk>/', Product_accountUpdateView.as_view(), name='edit_product_account'),
    path('delete-product_account/<int:pk>', Product_accountDeleteView.as_view(), name='delete_product_account'),
]