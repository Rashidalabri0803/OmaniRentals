from django import forms
from .models import Property, Tenant, Lease

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('title', 'address', 'city', 'rent_price', 'description')
        labels = {
            'title': 'عنوان العقار',
            'address': 'العنوان',
            'city': 'المدينة',
            'rent_price': 'سعر الإيجار',
            'description': 'الوصف',
        }


class TenantForm(forms.ModelForm):
    class Meta:
        model = Tenant
        fields = ('full_name', 'phone', 'email')
        labels = {
            'full_name': 'الاسم الكامل',
            'phone': 'رقم الهاتف',
            'email': 'البريد الإلكتروني',
        }


class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = ('property', 'tenant', 'start_date', 'end_date', 'rent_amount')
        labels = {
            'property': 'العقار',
            'tenant': 'المستأجر',
            'start_date': 'تاريخ البدء',
            'end_date': 'تاريخ الانتهاء',
            'rent_amount': 'مبلغ الإيجار',
        }