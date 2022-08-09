from django.db import models

# Create your models here.
class Post(models.Model):
    user = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
