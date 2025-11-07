from django.contrib import admin
from .models import BillingRecord

# Register your models here.

@admin.register(BillingRecord)
class BillingRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'billing_date', 'paid', 'created_at')
    list_filter = ('paid',)
    search_fields = ('patient__first_name', 'patient__last_name')
