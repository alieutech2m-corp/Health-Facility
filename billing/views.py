from django.shortcuts import render
from .serializers import BillingRecordSerializer
from rest_framework import generics, permissions, viewsets
from .models import BillingRecord

# Create your views here.
class BillingRecordViewSet(viewsets.ModelViewSet):
    """
      billing management for patient.
      """
    queryset = BillingRecord.objects.select_related('patient').all()
    serializer_class = BillingRecordSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Admins can see all billing records.
        Patients can see only their own billing records.
        """
        user = self.request.user
        if user.is_staff:
            return BillingRecord.objects.all()
        return BillingRecord.objects.filter(patient_email=user.email)