from django.db import models
from cloudinary.models import CloudinaryField

class Writer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class NewsArticle(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title