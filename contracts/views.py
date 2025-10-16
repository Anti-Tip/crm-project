from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Contract
from .forms import ContractForm


@login_required
@permission_required('contracts.view_contract', raise_exception=True)
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'contracts/contracts-list.html', {'contracts': contracts})


@login_required
@permission_required('contracts.view_contract', raise_exception=True)
def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'contracts/contracts-detail.html', {'contract': contract})


@login_required
@permission_required('contracts.add_contract', raise_exception=True)
def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Контракт создан успешно.')
            return redirect('contracts:contract_list')
    else:
        form = ContractForm()
    return render(request, 'contracts/contracts-create.html', {'form': form})


@login_required
@permission_required('contracts.change_contract', raise_exception=True)
def contract_edit(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            messages.success(request, 'Контракт обновлен успешно.')
            return redirect('contracts:contract_detail', pk=pk)
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/contracts-edit.html', {'form': form, 'contract': contract})


@login_required
@permission_required('contracts.delete_contract', raise_exception=True)
def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        messages.success(request, 'Контракт удален успешно.')
        return redirect('contracts:contract_list')
    return render(request, 'contracts/contracts-delete.html', {'contract': contract})
