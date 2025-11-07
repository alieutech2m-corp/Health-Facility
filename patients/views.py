from django.shortcuts import render
from .serializers import PatientSerializer, MedicalRecordSerializer
from .models import Patient, MedicalRecord
from rest_framework import generics, permissions, viewsets
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    """
    Provides ALL CRUD actions:
    list, retrieve, create, update, partial_update, destroy
    """
    queryset = Patient.objects.all().order_by('-created_at')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MedicalRecordListCreateView(generics.ListCreateAPIView):
    """View to list and create medical records for a specific patient."""
    serializer_class = MedicalRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return MedicalRecord.objects.filter(patient__id=patient_id)

    def perform_create(self, serializer):
        patient_id = self.kwargs['patient_id']
        serializer.save(patient_id=patient_id)