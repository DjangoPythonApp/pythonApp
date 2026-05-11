from django.shortcuts import render
from django.http import HttpRequest,HttpResponse


def index(request:HttpRequest):

    context={}
    message=''

    if request.method == 'POST':

        year:str = request.POST.get('data')

        if year == '':
             message='Enter the valid  Year!!!'

             context ={
                "message":message
             }

             return render(request,'index.html',context)

        try:
            yearr:int=int(year)
            print(type(yearr))
            print(yearr)

        except Exception as e:
            message='Enter the valid  Year!!!'

            context ={
                "message":message
             }
            return render(request,'index.html',context)
            

        if yearr%400 == 0:
            print("True")
            message=f'{yearr} is a century leapyear.'
        elif yearr%4 == 0 and yearr%100 != 0:
            print("False")
            message=f'{yearr} is a non-century leapyear.'

        else:

            message=f'{yearr} is not a leapyear.'
        

    context ={

        "message":message
    }







    return render(request,'index.html',context)