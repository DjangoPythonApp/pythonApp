
from django.urls import path
from .views import create, read, edit, delete
urlpatterns = [
   
   path('',create, name='insert'),
   path('displayList/',read, name='display_list'),
   path('edit_list_path/<int:id>/',edit, name='edit_page'),
   path('delete_path/<int:id>/',delete,name='delete_page_ano')
]
