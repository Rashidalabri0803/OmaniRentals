from django.db import models
from django.utils.translation import gettext_lazy as _


class Property(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('عنوان العقار'))
    address = models.CharField(max_length=255, verbose_name=_('العنوان'))
    city = models.CharField(max_length=100, verbose_name=_('المدينة'))
    rent_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('سعر الإيجار'))
    description = models.TextField(verbose_name=_('الوصف'))

    def __str__(self):
        return self.title

class Tenant(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_('الاسم الكامل'))
    phone = models.CharField(max_length=20, verbose_name=_('رقم الهاتف'))
    email = models.EmailField(verbose_name=_('البريد الإلكتروني'))

    def __str__(self):
        return self.full_name

class Lease(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name=_('العقار'))
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name=_('المستأجر'))
    start_date = models.DateField(verbose_name=_('تاريخ البدء'))
    end_date = models.DateField(verbose_name=_('تاريخ الانتهاء'))
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('مبلغ الإيجار'))

    def __str__(self):
        return f"{self.tenant.full_name} - {self.property.title}"