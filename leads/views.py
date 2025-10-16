from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Lead
from .forms import LeadForm


@login_required
@permission_required('leads.view_lead', raise_exception=True)
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/leads-list.html', {'leads': leads})


@login_required
@permission_required('leads.view_lead', raise_exception=True)
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/leads-detail.html', {'lead': lead})


@login_required
@permission_required('leads.add_lead', raise_exception=True)
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Потенциальный клиент создан успешно.')
            return redirect('leads:lead_list')
    else:
        form = LeadForm()
    return render(request, 'leads/leads-create.html', {'form': form})


@login_required
@permission_required('leads.change_lead', raise_exception=True)
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Потенциальный клиент обновлен успешно.')
            return redirect('leads:lead_detail', pk=pk)
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads/leads-edit.html', {'form': form, 'lead': lead})


@login_required
@permission_required('leads.delete_lead', raise_exception=True)
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        messages.success(request, 'Потенциальный клиент удален успешно.')
        return redirect('leads:lead_list')
    return render(request, 'leads/leads-delete.html', {'lead': lead})


@login_required
@permission_required('leads.change_lead', raise_exception=True)
def lead_to_customer(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return redirect('customers:customer_create', lead_pk=lead.pk)
