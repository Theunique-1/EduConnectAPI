from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Tutors(AbstractUser):
    profile_picture = models.ImageField(upload_to='tutor_pictures/', null=True, blank=True)
    expertise = models.CharField(max_length=300)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    online_availability = models.BooleanField(default=False)
    in_person_availability = models.BooleanField(default=False)
    location = models.CharField(max_length=300, null=False, blank=False)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="tutors_groups", 
        related_query_name="tutor",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="tutors_user_permissions", 
        related_query_name="tutor",
    )

    def __str__(self):
        return self.username