from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# Create your views here.
from .forms import StudentRegistration
def index(request:HttpRequest) -> HttpResponse:

    form = StudentRegistration()
    return render(request, 'index.html',{"form":form})
