from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):

    context = {}

    message = ''
    error = ''

    if request.method == 'POST':

        text: str = request.POST.get('name')

        if text == '':
            error = "Please enter the data..."

        else:
            words: list = text.split()

            new_list = []

            for i in words:
                result = i.capitalize()
                new_list.append(result)

            message = ' '.join(new_list)

        context = {
            "error": error,
            "message": message
        }

    return render(request, 'index.html', context)