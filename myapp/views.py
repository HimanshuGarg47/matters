from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status

from .serializers import *

class DoctorSignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = DoctorSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class DoctorLoginView(generics.CreateAPIView):
    serializer_class = DoctorSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({"message": "Login successful"})
        else:
            return Response({"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        

class CustomUserSignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

class CustomUserLoginView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return Response({"message": "Login successful"})
        else:
            return Response({"message": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)