from django.urls import path
from . import views

urlpatterns = [
    path('',views.feedback_form,name='feedback_form'),
    path('success/', views.feedback_success, name='feedback_success'),
    path('analyze/',views.analyze_feedback, name='analyze_feedback'
    ),
]