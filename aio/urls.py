from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('<str:chat_name>/', views.chat),
]