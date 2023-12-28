from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.displayFeed),
    path('home/', views.displayFeed),
    path('feed/', views.displayFeed, name='all'),
]