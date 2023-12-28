from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    user = get_user_model()
    author = models.ForeignKey(user, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
