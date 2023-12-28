from django.shortcuts import render
from post import models
from django.views.generic import ListView, DetailView

# Create your views here.

class DisplayFeed(ListView):
    model = models.Post
    template_name = 'feed/feed.html'

class ViewPost(DetailView):
    model = models.Post
    template_name = 'post/post_viewer.html'
    context_object_name = 'post'