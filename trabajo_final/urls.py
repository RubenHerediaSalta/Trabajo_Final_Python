from django.contrib import admin
from django.urls import path, include

from trabajo_final.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

from trabajo_final.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('controlpanel/', controlpanel),
    path('about/', about),

    path('product_account/', include('product_account.urls')),
    path('product_coaching/', include('product_coaching.urls')),
    path('coaches/', include('coaches.urls')),
    path('users/', include('users.urls')),
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
