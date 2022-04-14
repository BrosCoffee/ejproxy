from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, default='/')
    date_added = models.DateTimeField()
