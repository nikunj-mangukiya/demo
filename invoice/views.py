from invoice.models import Invoice
from invoice.serializers import (
    AllInvoiceSerializer,
    InvoiceSerializer,
    InvoiceItemSerializer,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse


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
        invoice = Invoice.objects.all()
        serializer = AllInvoiceSerializer(invoice, many=True)
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
