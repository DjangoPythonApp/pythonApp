from django.urls import path
from . import views, views_api

urlpatterns = [
    # Template Views
    path('', views.category_list, name='category_list'),
    path('add/', views.add_category, name='add_category'),
    path('edit/<int:id>/', views.edit_category, name='edit_category'),
    path('delete/<int:id>/',views.delete_category,name='delete_category'),


    # REST API
    path('api/add/', views_api.api_add_category, name='api_add_category'),
    path('api/list/', views_api.api_list_categories, name='api_list_categories'),
    path('api/update/<int:pk>/', views_api.api_update_category, name='api_update_category'),
    path('api/delete/<int:pk>/', views_api.api_delete_category, name='api_delete_category'),
]