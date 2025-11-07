from django.db import models
from patients.models import Patient

# Create your models here.
class BillingRecord(models.Model):
    """Model representing a billing record for a patient."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='billing_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateField()
    description = models.TextField()
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the BillingRecord model."""
        return f"Billing Record for {self.patient.first_name} {self.patient.last_name} on {self.billing_date} - Amount: {self.amount}"
    
    class Meta:
        verbose_name = "Billing Record"
        verbose_name_plural = "Billing Records"
