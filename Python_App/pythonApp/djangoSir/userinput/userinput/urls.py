from django.contrib import admin
from django.urls import path, include

from .views import home, edit_view, delete_view

urlpatterns = [
    path('', home, name='home'),
    path('edit/<int:item_id>/', edit_view, name='edit'),   # ✅ no '/'
    path('delete/<int:item_id>/', delete_view, name='delete'),
    path('admin/', admin.site.urls),                      # ✅ correct
]