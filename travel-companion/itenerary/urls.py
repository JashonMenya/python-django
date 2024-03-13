from django.urls import path

from . import views

urlpatterns = [
    path('itenerary', views.itenerary)
]