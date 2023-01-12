from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def coming_soon(request):
    return render(request, 'ecommerce/coming_soon.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ecommerce/product_detail.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:product_list')
    else:
        form = ProductForm()
    return render(request, 'ecommerce/product_form.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('ecommerce:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'ecommerce/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('ecommerce:product_list')
