from django.db import models

# Create your models here.

class Patient(models.Model):
    """Model representing a patient in the health facility."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    addres = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Patient model."""
        return f"{self.first_name} {self.last_name} ({self.medical_record_number})"
    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

class MedicalRecord(models.Model):
    """Model representing a medical record for a patient."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    record_date = models.DateField()
    description = models.TextField()
    treatment = models.TextField()
    doctor_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name} on {self.record_date}"
    
    class Meta:
        verbose_name = "Medical Record"
        verbose_name_plural = "Medical Records"   

