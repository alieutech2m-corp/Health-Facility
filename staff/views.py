from django.shortcuts import render
from .serializers import StaffSerializer
from .models import Doctor
from rest_framework import generics, permissions, viewsets

# Create your views here.

class StaffViewSet(viewsets.ModelViewSet):
    """Perform all CRUD operations on staff members."""
    queryset = Doctor.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



