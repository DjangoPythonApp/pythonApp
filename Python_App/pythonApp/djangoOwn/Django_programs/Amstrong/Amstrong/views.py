from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def index(request:HttpRequest) -> HttpResponse:

    context={}
    sum1=0
    rem=0

    if request.method == 'POST':
        num = request.POST.get('num')

        if num == '':
            error = 'enter the value!!!'

            return render(request,'index.html',context={'error':error})


        new_num=int(num)

        x = new_num

        while x!=0:
            rem = x%10
            sum1+=rem**3
            x//=10

        if sum1 == new_num:
            message=f'{new_num} is Amstrong number.'
        else:
            message=f'{new_num} is not Amstrong number.'


        context={

            "message":message
        }





    return render(request, 'index.html',context)