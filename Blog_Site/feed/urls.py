from django.urls import path
from . import views

urlpatterns = [
    path('', views.displayFeed, name='feed'),
    path('feed', views.displayFeed, name='feed'),
]