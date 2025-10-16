from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Advertisement
from .forms import AdvertisementForm


@login_required
@permission_required('advertisements.view_advertisement', raise_exception=True)
def advertisement_list(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'ads/ads-list.html', {'advertisements': advertisements})


@login_required
@permission_required('advertisements.view_advertisement', raise_exception=True)
def advertisement_detail(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'ads/ads-detail.html', {'advertisement': advertisement})


@login_required
@permission_required('advertisements.add_advertisement', raise_exception=True)
def advertisement_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Рекламная кампания создана успешно.')
            return redirect('advertisements:advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'ads/ads-create.html', {'form': form})


@login_required
@permission_required('advertisements.change_advertisement', raise_exception=True)
def advertisement_edit(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Рекламная кампания обновлена успешно.')
            return redirect('advertisements:advertisement_detail', pk=pk)
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'ads/ads-edit.html', {'form': form, 'advertisement': advertisement})


@login_required
@permission_required('advertisements.delete_advertisement', raise_exception=True)
def advertisement_delete(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        advertisement.delete()
        messages.success(request, 'Рекламная кампания удалена успешно.')
        return redirect('advertisements:advertisement_list')
    return render(request, 'ads/ads-delete.html', {'advertisement': advertisement})
