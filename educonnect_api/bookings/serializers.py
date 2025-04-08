from rest_framework import serializers
from .models import Booking
from users.models import Students
from tutors.models import Tutors

# Serializer for displaying basic student information
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'username']

# Serializer for displaying basic tutor information
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ['id', 'username']

# Main serializer for Booking objects, including nested student and tutor details
class BookingSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)   # Nested serializer to display student details
    tutor = TutorSerializer(read_only=True)     # Nested serializer to display tutor details
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Students.objects.all(), write_only=True, source='student'
    )
    tutor_id = serializers.PrimaryKeyRelatedField(
        queryset=Tutors.objects.all(), write_only=True, source='tutor'
    )

    class Meta:
        model = Booking
        fields = [
            'id', 'student', 'student_id', 'tutor', 'tutor_id', 'date_time',
            'duration', 'is_online', 'location', 'booking_status',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

# Serializer for creating new Booking objects
class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['student', 'tutor', 'date_time', 'duration', 'is_online', 'location']

# Serializer for updating existing Booking objects
class BookingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['date_time', 'duration', 'is_online', 'location']
        read_only_fields = ['student', 'tutor', 'created_at', 'updated_at']