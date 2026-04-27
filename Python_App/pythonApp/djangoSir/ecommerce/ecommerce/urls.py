from django.contrib import admin
from django.urls import path, include
from category import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),   # homepage
    path('category/', include('category.urls')),
]