from rest_framework import serializers
from .models import Doctor, CustomUser

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('email', 'password', 'age', 'profession', 'yearofexperience', 'expertise', 'fees_per_hour')
        extra_kwargs = {'password': {'write_only': True}}


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'age', 'profession')
        extra_kwargs = {'password': {'write_only': True}}