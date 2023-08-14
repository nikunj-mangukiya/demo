from .models import Invoice, InvoiceItem
from rest_framework import serializers


class InvoiceSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=True)

    class Meta:
        model = Invoice
        fields = ("date", "number", "id")


class InvoiceItemSerializer(serializers.ModelSerializer):
    units = serializers.IntegerField(required=True)
    description = serializers.CharField(max_length=255, required=True)
    amount = serializers.FloatField(required=True)
    invoice_id = serializers.IntegerField(required=True)

    class Meta:
        model = InvoiceItem
        fields = ("units", "description", "amount", "invoice_id")


class AllInvoiceSerializer(serializers.ModelSerializer):
    items = serializers.StringRelatedField(many=True)

    class Meta:
        model = Invoice
        fields = ("date", "number", "id", "items")


class AllInvoiceItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ("id", "units", "description", "amount")
