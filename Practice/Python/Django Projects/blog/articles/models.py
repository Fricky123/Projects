from django.db import models
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100, null=True, blank= True)
    slug = models.SlugField(null=True, blank= True)
    body = models.TextField(null=True, blank= True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    