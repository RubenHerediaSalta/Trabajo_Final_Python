from django.urls import path
from product_coaching.views import *


urlpatterns = [
    path('controlpanel-product_coaching/', controlpanel, name='controlpanel_product_coaching'),
    path('create-product_coaching/', Product_coachingCreateView.as_view(), name='add_product_coaching'),
    path('list-product_coaching', list_product_coaching, name='list_product_coaching'),
    path('update-product_coaching/<int:pk>/', Product_coachingUpdateView.as_view(), name='edit_product_coaching'),
    path('delete-product_coaching/<int:pk>', Product_coachingDeleteView.as_view(), name='delete_product_coaching'),
]