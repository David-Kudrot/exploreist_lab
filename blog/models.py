from django.db import models
from django.contrib.auth.models import User
from category.models import CategoryModel
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="blog/photos")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(CategoryModel)