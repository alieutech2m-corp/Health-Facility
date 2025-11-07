from django.db import models

# Create your models here.
class Doctor(models.Model):
    """Model representing a staff member in the health facility."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    speciality = models.CharField(max_length=120, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Staff model."""
        return f"{self.first_name} {self.last_name} - {self.position}"
    
    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"

