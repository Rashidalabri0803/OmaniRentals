from django.shortcuts import render, get_object_or_404, redirect
from .models import Property, Tenant, Lease
from .forms import PropertyForm, TenantForm, LeaseForm, PaymentForm
# Create your views here.

def dashbord(request):
    properties_count = Property.objects.count()
    tenants_count = Tenant.objects.count()
    active_leases = Lease.objects.filter(end_date__gte=date.today()).count()
    pending_payments = Payment.objects.filter(status='pending').count()

    context = {
        'properties_count': properties_count,
        'tenants_count': tenants_count,
        'active_leases': active_leases,
        'pending_payments': pending_payments,
    }
    return render(request, 'dashbord.html', context)
    
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'prop_list.html', {'properties': properties})

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant_list.html', {'tenants': tenants})

def lease_list(request):
    leases = Lease.objects.all()
    return render(request, 'lease_list.html', {'leases': leases})

def property_create(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_form.html', {'form': form})

def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_form.html', {'form': form})