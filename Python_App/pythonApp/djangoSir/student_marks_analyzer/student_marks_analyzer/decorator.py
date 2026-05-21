from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
def deco_fun(index:object)->object:

    def wrapper(request:HttpRequest) -> HttpResponse:

        inner_context = {}
        error=''
        error2=''

        fullName:str = request.POST.get('fullName')

        if fullName == '':
            error:str = 'enter the valid name..'

            inner_context = {
                "error":error,
            }

            return render(request, 'index.html',inner_context)

        marks:str = request.POST.get('marks')

        if marks == '':
            error2:str = 'invalid marks..'


            inner_context = {
                "error2":error2,
            }

            return render(request, 'index.html',inner_context)

        return index(request,fullName,marks)

    return wrapper




