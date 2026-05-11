from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):

   no1:int = 0
   no2:int = 0
   context = {}

   if request.method == 'POST':
      no1 = int(request.POST.get('num1'))
      no2 = int(request.POST.get('num2'))

      no1 = no1 + no2

      no2 = no1 - no2

      no1 = no1 - no2

      context ={
         'no1':no1,
         'no2':no2,
      }

   return render(request, 'index.html', context)