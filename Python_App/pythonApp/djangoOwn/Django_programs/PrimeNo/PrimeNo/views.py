from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:

    count:int=0
    context ={}
    error :str=''

    if request.method == 'POST':
        num =  request.POST.get('num')

        if num == '':
            error:str="Please enter the value!!!"

            return render(request, 'index.html',context={'error':error})

        new_num = int(num)

        for i in range(1,new_num+1):
            if new_num%i == 0:
                count+=1

        else:
            if count == 2:
                message:str=f'{new_num} Prime number.'
            else:
                message:str=f'{new_num} Not Prime number.'

        context={

            "message":message,
           
        }


    return render(request, 'index.html',context)