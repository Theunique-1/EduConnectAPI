from django.db import models
from users.models import Students
from tutors.models import Tutors

# Create your models here.

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]

    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    duration = models.IntegerField()
    is_online = models.BooleanField(default=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    booking_status = models.CharField(
        max_length=30,
        choices=BOOKING_STATUS_CHOICES,
        default='pending',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking {self.id} - {self.student.username} - {self.tutor.username}"