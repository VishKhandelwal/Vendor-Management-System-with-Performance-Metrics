
from django.urls import path
from .views import *


urlpatterns = [ 

    path('', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    path('', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),
]
