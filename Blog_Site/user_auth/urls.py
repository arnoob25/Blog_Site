from django.urls import path
from django.contrib.auth.views import LogoutView # remove this

from . import views


app_name = 'user_auth'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth.html'), name='logout'),
]