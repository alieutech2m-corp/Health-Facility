from rest_framework import serializers
from staff.serializers import StaffSerializer
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    """Serializer for Appointment model."""
    patient_details = StaffSerializer(source='patient', read_only=True)
    doctor_details = StaffSerializer(source='doctor', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'patient',
            'appointment_date',
            'doctor_name',
            'reason',
            'status',
            'created_at',
            'updated_at',
        ]
