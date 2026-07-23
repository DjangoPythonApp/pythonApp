from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

from category.decorators import prevent_duplicate_category
from .models import Category

# Home Page
def home(request):
    return render(request, 'home.html')

# CREATE
@prevent_duplicate_category
def add_category(request):
    if request.method == "POST":
        name: str = request.POST.get("name")
        description: str = request.POST.get("description")

        if name and description:
            try:
                Category.objects.create(name=name,description=description)

                return JsonResponse({
                    "success": True,
                    "message": "Category added successfully"
                })

            except Exception as e:
                return JsonResponse({
                    "success": False,
                    "message": str(e)
                })

        return JsonResponse({
            "success": False,
            "message": "All fields are required"
        })

    return render(request, "add_category.html")


# READ
def category_list(request):
    categories: QuerySet = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


@prevent_duplicate_category
def edit_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        category.name = name
        category.description = description
        category.save()

        return JsonResponse({
            "success": True,
            "message": "Category updated successfully"
        })

    return render(request,"add_category.html",{"category": category})


def delete_category(request, id):
    if request.method == "POST":
        try:
            category = Category.objects.get(id=id)
            category.delete()
            return JsonResponse({
                "success": True,
                "message": "Category deleted successfully"
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            })
    return JsonResponse({
        "success": False,
        "message": "Invalid request"
    })