from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm


@login_required
@permission_required('products.view_product', raise_exception=True)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/products-list.html', {'products': products})


@login_required
@permission_required('products.view_product', raise_exception=True)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/products-detail.html', {'product': product})


@login_required
@permission_required('products.add_product', raise_exception=True)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Услуга создана успешно.')
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/products-create.html', {'form': form})


@login_required
@permission_required('products.change_product', raise_exception=True)
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Услуга обновлена успешно.')
            return redirect('products:product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/products-edit.html', {'form': form, 'product': product})


@login_required
@permission_required('products.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Услуга удалена успешно.')
        return redirect('products:product_list')
    return render(request, 'products/products-delete.html', {'product': product})
