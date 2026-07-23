from django.urls import path

from . import views


app_name = "predictor"

urlpatterns = [
    path(
        "",
        views.placement_prediction,
        name="placement_prediction",
    ),
]