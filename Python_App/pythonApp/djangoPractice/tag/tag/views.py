from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def home(request:HttpRequest) -> HttpResponse:

    return render(request, 'webPages/home.html')


def about(request:HttpRequest) -> HttpResponse:

    return render(request, 'webPages/about.html')


def contacts(request:HttpRequest) -> HttpResponse:

    return render(request, 'webPages/contacts.html')