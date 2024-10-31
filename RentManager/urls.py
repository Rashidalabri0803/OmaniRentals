from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('tenants/', views.tenant_list, name='tenant_list'),
    path('leases/', views.lease_list, name='lease_list'),
    path('properties/new/', views.property_create, name='property_create'),
    path('properties/<int:pk>/edit/', views.property_update, name='property_update'),
]