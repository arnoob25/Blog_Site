from django.urls import path
from . import views

app_name = 'post'

# create paths here

urlpatterns = [
    path('create/', views.CreatePost.as_view(), name = 'create'),
    path('edit/<pk>/', views.EditPost.as_view(), name = 'edit'),
    path('delete/<pk>/', views.DeletePost.as_view(), name = 'delete'),
]