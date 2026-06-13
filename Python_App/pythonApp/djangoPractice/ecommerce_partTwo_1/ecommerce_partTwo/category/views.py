from django.shortcuts import render, redirect
from .models import Category

# Home Page
def home(request):
    return render(request, 'home.html')

# CREATE
def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        number = request.POST.get('number')

        Category.objects.create(
            name=name,
            description=description,
            number=number
        )

        return redirect('category_list')

    return render(request, 'add_category.html')


# READ
def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        'category_list.html',
        {'categories': categories}
    )


# UPDATE
def edit_category(request, id):
    category = Category.objects.get(id=id)

    qty_range = range(1, category.number + 1)

    if request.method == "POST":
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')

        category.number = request.POST.get('quantity')
        print("Selected Quantity:", category.number)

        category.save()

        return redirect('category_list')

    return render(
        request,
        'edit_category.html',
        {
            'category': category,
            'qty_range': qty_range
        }
    )


# DELETE
def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()

    return redirect('category_list')