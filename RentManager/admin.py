from django.contrib import admin

from .models import Lease, Property, Tenant


# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'city', 'rent_price')
    list_filter = ('title', 'city')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email')
    list_filter = ('full_name', 'phone')

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'property', 'start_date', 'end_date', 'rent_amount')
    list_filter = ('start_date', 'end_date')