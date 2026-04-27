from django.http import HttpResponse
from django.shortcuts import render

# def home(request):
#     return HttpResponse("Hello, World!")

def home(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is the about page.")

def aboutDetails(request, name):
    return HttpResponse(f"Details of {name}")