from . import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CreatePost(LoginRequiredMixin, CreateView):
    model = models.Post
    template_name = 'post/post_editor.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('feed:post', kwargs = {'pk':self.object.pk})

class EditPost(LoginRequiredMixin, UpdateView):
    model = models.Post
    template_name = 'post/post_editor.html'
    fields = ['title', 'content']

    # ensure a hacker cannot edit others' posts
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
    def get_success_url(self):
        return reverse('feed:post', kwargs = {'pk':self.object.pk})
    
class DeletePost(LoginRequiredMixin, DeleteView):
    model = models.Post
    template_name = 'post/post_editor.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('feed:all')
    
    # ensure a hacker cannot delete others' posts
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    