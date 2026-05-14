from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest):
    context ={}
    message=''
    my_name=''
    dispaly=''
    my_name=''
    concat_str=''
    if request.method == 'POST':

        name:str = request.POST.get('name')
        if name == '':
            message:str = 'Please enter the name..'

        else:
            new_name:str=name.lstrip()
            new_name2:str=name.rstrip()
            

            dispaly:str = f'Hello, {new_name2}.'

        context = {
            "message":message,
            "display":dispaly
        }


    return render(request, 'index.html',context)