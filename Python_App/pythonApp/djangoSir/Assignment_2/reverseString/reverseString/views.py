from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request:HttpRequest):

    context = {}
    error = ''
    reverse_str =''
    name=''

    if request.method == 'POST':

        name:str = request.POST.get('name')

        if name == '':
            error:str = 'enter the data...'
        n:int = len(name)
        new_array:list =[]
        n1=n-1
        while n1 != -1:

            new_array.append(name[n1])
            n1-=1

        reverse_str = ''.join(new_array)
        
        context ={
            "new_array":new_array
        }

    context = {
        "name":name,
        "reverseString":reverse_str,
        "error":error
    }


    return render(request, 'index.html',context)