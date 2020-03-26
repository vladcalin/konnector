from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    full_name = models.CharField(max_length=100, blank=True, default='')

    def get_full_name(self):
        return self.full_name
