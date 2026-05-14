from django.shortcuts import render
from django.http import HttpRequest

def index(request: HttpRequest):

    message = ''
    error = ''

    context = {}

    if request.method == "POST":

        string_1: str = request.POST.get('name')
        string_2: str = request.POST.get('name2')

        if string_1 == '' or string_2 == '':
            error = 'Please insert the data...'

        else:
            st_1: str = string_1.lower()
            st_2: str = string_2.lower()

            if st_1 == st_2:
                message = f'Both strings are same. String one: {string_1} and string two: {string_2}.'
            else:
                message = f'Both strings are not same. String one: {string_1} and string two: {string_2}.'

        context = {
            "message": message,
            "error": error
        }

    return render(request, 'index.html', context)