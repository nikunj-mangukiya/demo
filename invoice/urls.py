from django.urls import path
from .views import InvoiceViews, InvoiceItemsViews


urlpatterns = [
    path("invoice/", InvoiceViews.as_view()),
    # path("invoice/<int:id>", InvoiceViews.as_view()),
    path("invoice-items/", InvoiceItemsViews.as_view()),
    # path("invoice-items/<int:id>", InvoiceItemsViews.as_view()),
]
