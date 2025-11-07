from django.shortcuts import render
from .serializers import AppointmentSerializer
from .models import Appointment
from rest_framework import generics, permissions, viewsets

# Create your views here.

class AppointmentSet(viewsets.ModelViewSet):
    """
    Appointment between patient and doctor.
    Perform CRUD operation for appointment.
    Authenticated users can create, view, update, and delete appointments.
    """
    queryset = Appointment.objects.select_related('patient', 'doctor').all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Doctors can see all appointments.
        Patients can see only their own appointments.
        """
        user = self.request.user
        if user.is_staff:
            return Appointment.objects.all()
        return Appointment.objects.filter(patient_email=user.email)