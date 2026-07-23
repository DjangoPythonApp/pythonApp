
from django.urls import path
from .views import home, form, category_list, edit_category,delete_category
urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('categoy_list/',category_list,name='category_list'),
    path('edit/<int:id>/' ,edit_category, name='edit_category'),
     path('delete/<int:id>/' ,delete_category, name='delete_category')
]
