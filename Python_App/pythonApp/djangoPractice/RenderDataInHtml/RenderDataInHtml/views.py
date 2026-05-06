from django.http  import HttpResponse
from django.shortcuts import render


def Home(request):
    dict: dict ={
        "name": "Subham Chakraborty",
        "age": 22,
        "hobbies": ["Coding", "Gaming", "Traveling"],
        "list2": [10, 20, 30, 40, 50]
    }

    
    return render(request, "index.html",dict)

def About(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contacts.html")