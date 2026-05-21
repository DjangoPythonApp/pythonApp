from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def deco_fun(index:object)->object:

    def wrapper(request:HttpRequest) -> HttpResponse:
        
        error:str = ''
        inner_context:dict={}
        data:str=''

        if request.method == 'POST':

            data:str = request.POST.get('data')

            if data == '':

                error:str = 'invalid entry..'

                inner_context : dict = {

                    "error":error
                }

                return render(request, 'index.html',inner_context)


        return index(request,data)

    return wrapper
