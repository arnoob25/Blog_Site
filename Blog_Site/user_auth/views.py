from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


# Create your views here.

class SignUp(CreateView):
    model = get_user_model()
    template_name = 'auth.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        # Save the user first
        response = super().form_valid(form)
        
        # Get the username and password
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        
        # Authenticate the user
        user = authenticate(self.request, username=username, password=password)
        
        # Log in the user if they are authenticated
        if user is not None:
            login(self.request, user)
        
        return response

class Login(LoginView):
    template_name = 'auth.html'
    success_url = reverse_lazy('feed')

class Logout(LogoutView):
    template_name = 'auth.html'
    next_page = 'feed'