from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE, null=True, blank=True)
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, null=True, blank=True)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'مستأجر'
        verbose_name_plural = 'مستأجرين'

    def __str__(self):
        return self.username

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'عقار'
        verbose_name_plural = 'عقارات'

    def __str__(self):
        return self.name

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name = 'مستأجر'
        verbose_name_plural = 'مستأجرين'

    def __str__(self):
        return self.name

class Contract(models.Model):
    property = models.ForeignKey('Property', on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'عقد'
        verbose_name_plural = 'عقود'

    def __str__(self):
        return f"{self.tenant} - {self.property}"

class Payment(models.Model):
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    class Meta:
        verbose_name = 'دفعة'
        verbose_name_plural = 'دفعات'

    def __str__(self):
        return f"{self.contract} - {self.amount}"