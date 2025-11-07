from django.db import models

# Create your models here.

class Medicine(models.Model):
    """Model representing a medicine in the pharmacy."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity_in_stock = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the Medicine model."""
        return f"{self.name} - {self.quantity_in_stock} in stock"
    
    class Meta:
        verbose_name = "Medicine"
        verbose_name_plural = "Medicines"
