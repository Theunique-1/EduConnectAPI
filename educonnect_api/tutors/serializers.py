from rest_framework import serializers
from .models import Tutors

class TutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutors
        fields = ('id', 'username', 'email', 'password', 'profile_picture', 'expertise', 'hourly_rate', 'online_availability', 'in_person_availability', 'location')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def validate_hourly_rate(self, value):
        if value < 0:
            raise serializers.ValidationError("Hourly rate cannot be negative.")
        return value