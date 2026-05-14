from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    context ={}
    message=''
    my_name=''
    dispaly=''
    if request.method == 'POST':

        name:str = request.POST.get('name')
        if name == '':
            message:str = 'Please enter the name..'

        else:
            new_name:str=name.strip()

            dispaly:str = f'Hello, {new_name}.'

        context = {
            "message":message,
            "display":dispaly
        }


    return render(request, 'index.html',context)