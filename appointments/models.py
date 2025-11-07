from django.db import models
from staff.models import Doctor
from patients.models import Patient

# Create your models here.

class Appointment(models.Model):
    """Model representing an appointment in the health facility."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    staff = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], default='scheduled')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Appointment model."""
        return f"Appointment for {self.patient.first_name} {self.patient.last_name} with {self.staff.first_name} {self.staff.last_name} on {self.appointment_date}"
    
    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"