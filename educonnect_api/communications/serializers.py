from rest_framework import serializers
from .models import Message
from users.serializers import StudentProfileSerializer
from tutors.serializers import TutorProfileSerializer

class MessageSerializer(serializers.ModelSerializer):
    sender_student = serializers.SerializerMethodField()
    sender_tutor = serializers.SerializerMethodField()
    receiver_student = serializers.SerializerMethodField()
    receiver_tutor = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ('id', 'sender_student', 'sender_tutor', 'receiver_student', 'receiver_tutor', 'content', 'timestamp', 'is_read')
        read_only_fields = ('timestamp',)

    def get_sender_student(self, obj):
        return StudentProfileSerializer(obj.sender_student).data if obj.sender_student else None

    def get_sender_tutor(self, obj):
        return TutorProfileSerializer(obj.sender_tutor).data if obj.sender_tutor else None

    def get_receiver_student(self, obj):
        return StudentProfileSerializer(obj.recipient_student).data if obj.recipient_student else None

    def get_receiver_tutor(self, obj):
        return TutorProfileSerializer(obj.recipient_tutor).data if obj.recipient_tutor else None

    def create(self, validated_data):
        # Creation handled in views to set sender based on user type
        raise NotImplementedError("Message creation should be handled in the view.")

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.is_read = validated_data.get('is_read', instance.is_read)
        instance.save()
        return instance