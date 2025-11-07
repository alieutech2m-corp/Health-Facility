from django.contrib import admin
from .models import Patient, MedicalRecord

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'record_date', 'doctor_name', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor_name')