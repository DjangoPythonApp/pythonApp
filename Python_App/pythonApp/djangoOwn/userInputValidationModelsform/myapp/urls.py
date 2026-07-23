from django.urls import path
from .views import home, product_list, product_create, product_update, product_delete

urlpatterns = [
   
   path('', home, name='home'),
   path('products/', product_list, name='product_list'),
   path('products/create/', product_create, name='product_create'),
   path('products/<int:product_id>/update/', product_update, name='product_update'),
   path('products/<int:product_id>/delete/', product_delete, name='product_delete') 

]

