from rest_framework import serializers
from .models import Booking
from users.serializers import StudentsSerializer
from tutors.serializers import TutorsSerializer
from datetime import datetime

class BookingSerializer(serializers.ModelSerializer):
    student = StudentsSerializer(read_only=True)
    tutor = TutorsSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = ('id', 'student', 'tutor', 'date_time', 'duration', 'is_online', 'location', 'booking_status', 'created_at', 'updated_at')

    def validate_date_time(self, value):
        if value < datetime.now():
            raise serializers.ValidationError("Booking date must be in the future.")
        return value