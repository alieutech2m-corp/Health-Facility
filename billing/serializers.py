from rest_framework import serializers
from .models import BillingRecord
from patients.serializers import PatientSerializer

class BillingRecordSerializer(serializers.ModelSerializer):
    """Serializer for BillingRecord model."""
    patient_details = PatientSerializer(source='patient', read_only=True)
    class Meta:
        model = BillingRecord
        fields = [
            'id',
            'patient',
            'amount',
            'billing_date',
            'description',
            'status',
            'created_at',
            'updated_at',
        ]
    read_only_fields = ['created_at', 'updated_at']