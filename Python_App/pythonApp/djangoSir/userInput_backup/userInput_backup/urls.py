from django.contrib import admin
from django.urls import path

from .views import home, delete_view
urlpatterns = [
    path("", home, name="home"),
    path("delete/<int:item_id>/",delete_view, name="delete"),
    path("admin/", admin.site.urls),
   
]
