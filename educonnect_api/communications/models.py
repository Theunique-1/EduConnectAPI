from django.db import models
from users.models import Students
from tutors.models import Tutors

# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey('self', related_name='sent_messages', on_delete=models.CASCADE, null=True, blank=True)
    sender_student = models.ForeignKey(Students, related_name='sent_student_messages', on_delete=models.CASCADE, null=True, blank=True)
    sender_tutor = models.ForeignKey(Tutors, related_name='sent_tutor_messages', on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey('self', related_name='received_messages', on_delete=models.CASCADE, null=True, blank=True)
    receiver_student = models.ForeignKey(Students, related_name='received_student_messages', on_delete=models.CASCADE, null=True, blank=True)
    receiver_tutor = models.ForeignKey(Tutors, related_name='received_tutor_messages', on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.id} - {self.sender} to {self.receiver}"