from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string

from category.decorators import prevent_duplicate_category
from .models import Category

import os
from django.conf import settings

# Home Page
def home(request):
    return render(request, 'home.html')

# CREATE
@prevent_duplicate_category
def add_category(request):
    if request.method == "POST":
        name: str = request.POST.get("name")
        description: str = request.POST.get("description")
        category_image = request.FILES.get("category_image")

        if name and description:
            try:
                Category.objects.create(name=name,description=description, image=category_image)

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

    return render(request, "category/add_category.html")


# READ
def category_list(request):
    categories: QuerySet = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})


@prevent_duplicate_category
def edit_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        new_image = request.FILES.get("category_image")

        category.name = name
        category.description = description

        if new_image:
            # Delete old image if exists
            if category.image and os.path.isfile(category.image.path):
                os.remove(category.image.path)

            # Assign new image
            category.image = new_image
        category.save()

        return JsonResponse({
            "success": True,
            "message": "Category updated successfully"
        })

    return render(request,"category/add_category.html",{"category": category})


def delete_category(request, id):
    if request.method == "POST":
        try:
            # category = Category.objects.get(id=id)
            category = get_object_or_404(Category, pk=id)

            # Delete the image file from storage if it exists
            if category.image and category.image.name:  # Ensure it has a file
                image_path = os.path.join(settings.MEDIA_ROOT, category.image.name)
                if os.path.exists(image_path):
                    os.remove(image_path)

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


