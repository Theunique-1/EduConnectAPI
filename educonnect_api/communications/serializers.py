from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_student = serializers.SerializerMethodField()
    sender_tutor = serializers.SerializerMethodField()
    receiver_student = serializers.SerializerMethodField()
    receiver_tutor = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('id', 'sender', 'sender_student', 'sender_tutor', 'receiver', 'receiver_student', 'receiver_tutor', 'content', 'timestamp', 'is_read')

    def get_sender_student(self, obj):
        from users.serializers import StudentProfileSerializer 
        return StudentProfileSerializer(obj.sender_student).data

    def get_sender_tutor(self, obj):
        from tutors.serializers import TutorProfileSerializer
        return TutorProfileSerializer(obj.sender_tutor).data

    def get_receiver_student(self, obj):
        from users.serializers import StudentProfileSerializer 
        return StudentProfileSerializer(obj.receiver_student).data

    def get_receiver_tutor(self, obj):
        from tutors.serializers import TutorProfileSerializer
        return TutorProfileSerializer(obj.receiver_tutor).data