from rest_framework import serializers
from .models import Message
from users.serializers import StudentsSerializer
from tutors.serializers import TutorsSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender_student = StudentsSerializer(read_only=True)
    sender_tutor = TutorsSerializer(read_only=True)
    receiver_student = StudentsSerializer(read_only=True)
    receiver_tutor = TutorsSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'sender', 'sender_student', 'sender_tutor', 'receiver', 'receiver_student', 'receiver_tutor', 'content', 'timestamp', 'is_read')
