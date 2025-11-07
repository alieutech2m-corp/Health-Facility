from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .serializers import RegisterSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    """View for user registration."""
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]