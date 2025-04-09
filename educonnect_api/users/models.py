from django.contrib.auth.models import AbstractUser
from django.db import models

class Students(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'username'  

    def __str__(self):
        return self.username