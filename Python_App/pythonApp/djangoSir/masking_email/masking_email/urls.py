from django.contrib import admin
from django.urls import path
from masking_email import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home")
]
