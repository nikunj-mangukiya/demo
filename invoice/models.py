from django.db import models
import uuid


def generate_invoice_number():
    return f"INV-{uuid.uuid4().hex[:6].upper()}"


class Invoice(models.Model):
    date = models.DateField()
    number = models.CharField(max_length=255, default=generate_invoice_number)

    def __str__(self):
        return f"{self.number}"


class InvoiceItem(models.Model):
    units = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    amount = models.FloatField(default=0.0)
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} {self.amount}"
