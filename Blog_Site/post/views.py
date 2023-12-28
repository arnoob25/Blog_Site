from . import models
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class CreatePost(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'post/create_post.html'
    fields = ['title', 'content']
    