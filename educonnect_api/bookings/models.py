from django.db import models
from users.models import Students
from tutors.models import Tutors

class Booking(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='bookings_as_student')
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE, related_name='bookings_as_tutor')
    date_time = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration in minutes")
    is_online = models.BooleanField(default=False)
    location = models.CharField(max_length=300, blank=True, null=True)
    booking_status = models.CharField(
        max_length=20,
        choices=[
            ('PENDING', 'Pending'),
            ('CONFIRMED', 'Confirmed'),
            ('COMPLETED', 'Completed'),
            ('CANCELLED', 'Cancelled'),
        ],
        default='PENDING'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking for {self.student.username} with {self.tutor.username} on {self.date_time}"