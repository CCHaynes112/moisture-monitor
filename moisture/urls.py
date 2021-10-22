from django.urls import path
from . import views

urlpatterns = [
    path('moisture/', views.MoistureView.as_view(), name="moisture_view"),
]
