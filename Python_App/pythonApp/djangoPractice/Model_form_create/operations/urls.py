from django.contrib import admin
from django.urls import path
from .views import student_create_view, submit_view, student_list, student_details

urlpatterns = [
    path('add/',student_create_view, name='form'),
    path('submit/',submit_view, name='submit'),
    path('', student_list,name='student_list'),
    path('details/<int:pk>/',student_details, name='student_details')
]

