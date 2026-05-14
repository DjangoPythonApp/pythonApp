from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request:HttpRequest)-> HttpResponse:

    message=0
    error=''
    context={}

    if request.method == 'POST':

        sentance:str = request.POST.get('name')

        if sentance == '':
            error:str = 'Please enter the data...'

        else:

            result:list = sentance.split()

            print(result)

            count=0

            for i in result:
                count+=1

            message:int = count

        context = {

            "error":error,
            "message":message
        }

    return render(request, 'index.html',context)