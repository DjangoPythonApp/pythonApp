from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, 'home.html')

# CREATE + READ
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Product.objects.create(
            name=name,
            price=price,
            description=description
        )

        return redirect('product_list')

    return render(request, 'product_form.html')


# UPDATE
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'product_form.html', {'form': form})


# DELETE
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == "POST":
        product.delete()
        return redirect('product_list')

    return render(request, 'product_delete.html', {'product': product})