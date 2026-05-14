from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

def index(request: HttpRequest)->HttpResponse:

    message = ''
    error = ''

    context = {}

    if request.method == "POST":

        string_1: str = request.POST.get('name')
       
        if string_1 == '':
            error = 'Please insert the data...'

            context ={
                "message":error
            }



            return render(request, 'index.html',context)

        reverse = ""

        for ch in string_1:
    
            reverse = ch + reverse
    


        if string_1 == reverse:
            message = f'Palindrome {string_1} & {reverse}.'
        else:
             message = f'Not Palindrome {string_1} & {reverse}.'


        context = {
            "message": message,
            "error": error
        }

    return render(request, 'index.html', context)