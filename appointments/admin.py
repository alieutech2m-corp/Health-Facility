from django.contrib import admin
from .models import Appointment

# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'staff', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'staff')
    search_fields = ('patient__first_name', 'patient__last_name', 'staff__first_name', 'staff__last_name', 'status')