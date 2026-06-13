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

        Category.objects.create(name=name, description=description)
        return redirect('category_list')

    return render(request, 'add_category.html')


# READ
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})