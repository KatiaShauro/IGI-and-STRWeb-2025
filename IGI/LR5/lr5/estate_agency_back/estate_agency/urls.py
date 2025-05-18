from django.urls import path, re_path
from . import views
from .views import EmployeeCreateView, CustomerCreateView, OwnerCreateView, RealtyCreateView, RealtyUpdateView, \
    RealtyDeleteView, DealCreateView, DealUpdateView, DealDeleteView

urlpatterns = [
    path('employee/', EmployeeCreateView.as_view(), name="assign-employee"),
    path('customer/', CustomerCreateView.as_view(), name="assign-customer"),
    path('owner/', OwnerCreateView.as_view(), name="assign-owner"),
    path('estate-list', views.estates, name="estates-list"),
    path('my-estates', views.my_estates, name="my-estates"),
    re_path(r'^estate/(?P<id>\d+)/$', views.estate, name="realty-detail"),
    path('realty-add/', RealtyCreateView.as_view(), name="realty-add"),
    re_path(r'^estate-update/(?P<pk>\d+)/$', RealtyUpdateView.as_view(), name="realty-update"),
    re_path(r'^estate-delete/(?P<pk>\d+)/$', RealtyDeleteView.as_view(), name="realty-delete"),
    re_path(r'^deal-create/(?P<realty_pk>\d+)/$', DealCreateView.as_view(), name="deal-create"),
    re_path(r'^deal-update/(?P<pk>\d+)/$', DealUpdateView.as_view(), name="deal-update"),
    re_path(r'^deal-delete/(?P<pk>\d+)/$', DealDeleteView.as_view(), name="deal-delete"),
    path('deals/', views.deals, name="deals"),
    path('my-deals/', views.my_deals, name="my-deals"),
]