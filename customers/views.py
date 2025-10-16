from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Customer
from .forms import CustomerForm


@login_required
@permission_required('customers.view_customer', raise_exception=True)
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customers-list.html', {'customers': customers})


@login_required
@permission_required('customers.view_customer', raise_exception=True)
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customers-detail.html', {'customer': customer})


@login_required
@permission_required('customers.add_customer', raise_exception=True)
def customer_create(request, lead_pk=None):
    lead = None
    if lead_pk:
        lead = get_object_or_404(Lead, pk=lead_pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save()
            messages.success(request, 'Активный клиент создан успешно.')
            return redirect('customers:customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(initial={'lead': lead})
    return render(request, 'customers/customers-create.html', {'form': form, 'lead': lead})


@login_required
@permission_required('customers.change_customer', raise_exception=True)
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Активный клиент обновлен успешно.')
            return redirect('customers:customer_detail', pk=pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customers-edit.html', {'form': form, 'customer': customer})


@login_required
@permission_required('customers.delete_customer', raise_exception=True)
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Активный клиент удален успешно.')
        return redirect('customers:customer_list')
    return render(request, 'customers/customers-delete.html', {'customer': customer})
