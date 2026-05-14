from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):

    context = {}
    message = ''
    display = ''
    final = ''
    name=''

    if request.method == 'POST':

        name = request.POST.get('name')
        old = request.POST.get('old')
        new = request.POST.get('new')

        if name == '':
            message = 'Please enter the name..'

        else:

            new_name = name.strip()

            display = f'{new_name}.'

            final = display.replace(old, new)

        context = {
            "name":name,
            "message": message,
            "display": display,
            "final_display": final
        }

    return render(request, 'index.html', context)