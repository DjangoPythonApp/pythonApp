from django.contrib import admin
from django.urls import path

from userinput_validate import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
]
