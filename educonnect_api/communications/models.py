from django.db import models
from users.models import Students
from tutors.models import Tutors

class Message(models.Model):
    sender_student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='sent_messages', null=True, blank=True)
    sender_tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE, related_name='sent_messages', null=True, blank=True)
    recipient_student = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)
    recipient_tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE, related_name='received_messages', null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  


    def __str__(self):
        sender = self.sender_student.username if self.sender_student else (self.sender_tutor.username if self.sender_tutor else "System")
        recipient = self.recipient_student.username if self.recipient_student else (self.recipient_tutor.username if self.recipient_tutor else "Unknown")
        return f"Message from {sender} to {recipient} at {self.timestamp}"

    def save(self, *args, **kwargs):
        # Ensure only one sender and one recipient type is set
        if sum(bool(x) for x in [self.sender_student, self.sender_tutor]) != 1:
            raise ValueError("Message must have exactly one sender (student or tutor).")
        if sum(bool(x) for x in [self.recipient_student, self.recipient_tutor]) != 1:
            raise ValueError("Message must have exactly one recipient (student or tutor).")
        super().save(*args, **kwargs)