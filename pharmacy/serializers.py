from rest_framework import serializers
from .models import Medicine

class MedicationSerializer(serializers.ModelSerializer):
    """Serializer for Medication model."""
    class Meta:
        model = Medicine
        fields = [
            'id',
            'name',
            'description',
            'quantity_in_stock',
            'price_per_unit',
            'expiration_date',
            'created_at',
            'updated_at',
        ]
    read_only_fields = ['created_at', 'updated_at']