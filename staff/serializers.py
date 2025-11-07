from rest_framework import serializers
from .models import Doctor

class StaffSerializer(serializers.ModelSerializer):
    """Serializer for Staff model."""
    class Meta:
        model = Doctor
        fields = [
            'id',
            'first_name',
            'last_name',
            'speciality',
            'email',
            'phone',
            'is_active',
            'hire_date',
            'created_at',
            'updated_at',
        ]
