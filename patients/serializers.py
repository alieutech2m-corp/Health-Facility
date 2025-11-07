from .models import Patient, MedicalRecord
from rest_framework import serializers
class MedicalRecordSerializer(serializers.ModelSerializer):
    """Serializer for MedicalRecord model."""
    class Meta:
        model = MedicalRecord
        fields = [
            'id',
            'patient',
            'record_date',
            'description',
            'treatment',
            'doctor_name',
            'created_at',
            'updated_at',
        ]
class PatientSerializer(serializers.ModelSerializer):
    """Serializer for Patient model."""
    medical_records = MedicalRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = [
            'id',
            'first_name',
            'last_name',
            'gender',
            'email',
            'phone',
            'addres',
            'date_of_birth',
            'created_at',
            'updated_at',
            'medical_records',
            ]
        read_only_fields = ['medical_records']