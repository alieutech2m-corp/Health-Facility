from django.shortcuts import render
from .serializers import MedicationSerializer
from .models import Medicine
from rest_framework import generics, permissions, viewsets
# Create your views here.

class MedicationViewSet(viewsets.ModelViewSet):
    """medications management."""
    queryset = Medicine.objects.all().order_by('name')
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

