from invoice.models import Invoice
from invoice.models import InvoiceItem
from invoice.serializers import (
    AllInvoiceSerializer,
    InvoiceSerializer,
    InvoiceItemSerializer,
    AllInvoiceItemsSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def homepage(request):
    return HttpResponse("Welcome to invoice app")


class InvoiceViews(APIView):
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, format=None):
        """
        Return a list of all invoices.
        """
        id = request.GET.get("id")
        if not id:
            invoice = Invoice.objects.all()
            serializer = AllInvoiceSerializer(invoice, many=True)
        else:
            invoice = get_object_or_404(Invoice, id=id)
            serializer = AllInvoiceSerializer(invoice)
        return Response(serializer.data)


class InvoiceItemsViews(APIView):
    def post(self, request):
        serializer = InvoiceItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"status": "error", "data": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request, format=None):
        """
        Return a list of all invoice items
        """
        id = request.GET.get("id")
        if not id:
            invoice_items = InvoiceItem.objects.all()
            serializer = AllInvoiceItemsSerializer(invoice_items, many=True)
        else:
            invoice_item = get_object_or_404(InvoiceItem, id=id)
            serializer = InvoiceItemSerializer(invoice_item)
        return Response(serializer.data)
