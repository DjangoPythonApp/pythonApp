from django.contrib import admin
from django.urls import path

from userinput import views

urlpatterns = [
    path("", views.home, name='home'),
    path('edit/<int:item_id>/', views.edit_view, name='edit'),
    path('delete/<int:item_id>/', views.delete_view, name='delete'),
    path("admin/", admin.site.urls),
    # path("", views.home, name="home"),
    
]
