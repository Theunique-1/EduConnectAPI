from django.contrib.auth.models import AbstractUser
from django.db import models

class Tutors(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    expertise = models.CharField(max_length=255, null=True, blank=True)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='tutor_profiles/', null=True, blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=("groups"),
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="tutors_set",  
        related_query_name="tutor",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="tutors_set",  # Add a unique related_name (same as groups for consistency)
        related_query_name="tutor",
    )

    def __str__(self):
        return self.username