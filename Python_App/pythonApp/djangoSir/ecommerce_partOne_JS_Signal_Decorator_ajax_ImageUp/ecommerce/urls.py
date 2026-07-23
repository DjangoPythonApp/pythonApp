from django.contrib import admin
from django.urls import path, include
from category import views

from django.conf.urls.static import static
from ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   # homepage
    path('category/', include('category.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)