from rest_framework import serializers
from .models import Students
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Students
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'bio', 'location')

    def create(self, validated_data):
        user = Students.objects.create_user(**validated_data)
        user.is_active = True
        user.save()
        return user


class StudentLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['is_student'] = True
        return token



class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('profile_picture', 'bio', 'location')