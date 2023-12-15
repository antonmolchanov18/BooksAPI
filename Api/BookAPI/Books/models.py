from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")
    description = models.TextField(blank=False)
    author = models.CharField(max_length=255)
    date_publication = models.IntegerField()
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
