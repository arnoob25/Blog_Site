from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

class SignUp(CreateView):
    model = get_user_model()
    template_name = 'user_auth/auth.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('feed:all')

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
    template_name = 'user_auth/auth.html'
    pass

class Logout(LogoutView):
    pass