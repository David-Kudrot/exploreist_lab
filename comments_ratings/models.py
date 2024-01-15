from django.contrib.auth.models import User
from django.db import models
from blog.models import Post

# Create your models here.
class CommentModel(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User)