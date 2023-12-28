from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.DisplayFeed.as_view()),
    path('home/', views.DisplayFeed.as_view()),
    path('feed/', views.DisplayFeed.as_view(), name='all'),
    path('post/<pk>/', views.ViewPost.as_view(), name='post'),
]