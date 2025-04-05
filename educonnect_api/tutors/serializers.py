from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tutors
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer for tutor registration
class TutorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Tutors
        # Fields to include in the registration process.
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        # Create a new Tutor using the validated data.
        tutor = Tutors.objects.create_user(**validated_data)
        return tutor


class TutorLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_tutor'] = isinstance(user, Tutors)
        return token

# Serializer for tutor profile creation
    
class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ('profile_picture', 'expertise', 'hourly_rate', 'online_availability', 'in_person_availability', 'location')
        read_only_fields = ('username', 'email', 'first_name', 'last_name')

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()  