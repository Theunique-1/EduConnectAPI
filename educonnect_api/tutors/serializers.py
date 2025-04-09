from rest_framework import serializers
from .models import Tutors
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Serializer for tutor registration
class TutorRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Tutors
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone number', 'bio', 'location', 'expertise', 'hourly_rate', 'profile_picture')

    def create(self, validated_data):
        user = Tutors.objects.create_user(**validated_data)
        return user


# Serializer for tutor login, extending JWT's TokenObtainPairSerializer
class TutorLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_tutor'] = True
        return token


# Serializer for tutor profile information
class TutorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ('profile_picture', 'phone', 'bio', 'location', 'expertise', 'hourly_rate')  