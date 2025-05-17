from django.urls import path
from . import views
from .views import EmployeeCreateView, CustomerCreateView, OwnerCreateView

urlpatterns = [
    path('employee/', EmployeeCreateView.as_view(), name="assign-employee"),
    path('customer/', CustomerCreateView.as_view(), name="assign-customer"),
    path('owner/', OwnerCreateView.as_view(), name="assign-owner"),
]