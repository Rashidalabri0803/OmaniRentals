# Generated by Django 5.0.3 on 2024-10-31 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان العقار')),
                ('address', models.CharField(max_length=255, verbose_name='العنوان')),
                ('city', models.CharField(max_length=100, verbose_name='المدينة')),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر الإيجار')),
                ('description', models.TextField(verbose_name='الوصف')),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='الاسم الكامل')),
                ('phone', models.CharField(max_length=20, verbose_name='رقم الهاتف')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الإلكتروني')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='تاريخ البدء')),
                ('end_date', models.DateField(verbose_name='تاريخ الانتهاء')),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='مبلغ الإيجار')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentManager.property', verbose_name='العقار')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RentManager.tenant', verbose_name='المستأجر')),
            ],
        ),
    ]