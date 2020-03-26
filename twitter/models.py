from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class TwitterIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    api_key = models.CharField(max_length=100)
    api_secret_key = models.CharField(max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)
