from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Product
from .forms import ProductForm

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request: HttpRequest) -> HttpResponse:
    form = ProductForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})


def product_update(request: HttpRequest, product_id: int) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product_form.html', {'form': form, 'product_id': product_id})



def product_delete(request: HttpRequest, product_id: int) -> HttpResponse:  
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        # Handle product deletion here
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'form': form, 'product_id': product_id, 'product': product})
