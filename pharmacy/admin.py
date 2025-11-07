from django.contrib import admin
from .models import Medicine

# Register your models here.
@admin.register(Medicine)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity_in_stock', 'price_per_unit', 'created_at')
    search_fields = ('name', 'description')
