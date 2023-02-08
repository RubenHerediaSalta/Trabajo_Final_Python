from django.urls import path
from coaches.views import *


urlpatterns = [
    path('controlpanel-coaches/', controlpanel, name='controlpanel_coaches'),
    path('create-coaches/', CoachesCreateView.as_view(), name='add_coaches'),
    path('list-coaches', list_coaches, name='list_coaches'),
    path('update-coaches/<int:pk>/', CoachesUpdateView.as_view(), name='edit_coaches'),
    path('delete-coaches/<int:pk>', CoachesDeleteView.as_view(), name='delete_coaches'),
]