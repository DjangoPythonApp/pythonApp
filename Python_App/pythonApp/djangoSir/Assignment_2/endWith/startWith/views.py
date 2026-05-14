from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request:HttpRequest):
    context:dict = {}
    error:str=''
    error2=''
    message:str=''

    if request.method == "POST":

        string:str = request.POST.get('name')
        substring:str = request.POST.get('name2') 

        if string == '' :
            error:str = 'Enter the string!!!'
            
        if substring == '':
            error2:str = 'Enter the string!!!'

        else:

            if string.endswith(substring):
                message:str = 'Sub-string is present in the string...'

            else:
                message:str = 'Sub-string is not present in the string...'

        context = {

            "error":error,
            "error2":error2,
            "message":message
        }   


    return render(request, 'index.html',context)