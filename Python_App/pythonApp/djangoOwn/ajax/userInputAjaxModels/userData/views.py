from django.shortcuts import  render
from django.http import HttpResponse,HttpRequest
from django.http import JsonResponse
from .models import GeneralModel

def home(request:HttpRequest) -> HttpResponse:
    return render(request,'home.html')

def form(request:HttpRequest) -> HttpResponse:
    if request.method == "POST":
        name: str = request.POST.get("name")
        email: str = request.POST.get("email")
        address: str = request.POST.get("address")
        age:str = request.POST.get("age")

        if name and email and address and age:
            try:
                GeneralModel.objects.create(name=name,email=email,address=address,age=age)

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

    categories = GeneralModel.objects.all()
    return render(request, "form.html", {"categories": categories})


# READ
def category_list(request:HttpRequest) ->HttpResponse:
    categories = GeneralModel.objects.all()
    return render(request, 'form.html', {'categories': categories})



def edit_category(request, id):
    category = GeneralModel.objects.get(id=id)

    if request.method == "POST":
        name: str = request.POST.get("name")
        email: str = request.POST.get("email")
        address: str = request.POST.get("address")
        age:str = request.POST.get("age")
        

        category.name = name
        category.email = email
        category.address = address
        category.age = age
        category.save()

        return JsonResponse({
            "success": True,
            "message": "Category updated successfully"
        })

    categories = GeneralModel.objects.all()
    return render(request, "form.html", {
        "category": category,
        "categories": categories,
    })


def delete_category(request, id):
    if request.method == "POST":
        try:
            category = GeneralModel.objects.get(id=id)
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
