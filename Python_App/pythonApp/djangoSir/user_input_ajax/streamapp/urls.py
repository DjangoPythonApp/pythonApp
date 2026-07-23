from django.urls import path
from .views import addStream

urlpatterns = [
    path('', addStream, name='add'),
]



