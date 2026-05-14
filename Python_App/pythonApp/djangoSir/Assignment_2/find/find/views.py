from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:

    context = {}

    if request.method == 'POST':

        main_string = request.POST.get('name')
        sub_string = request.POST.get('find1')

        position = main_string.find(sub_string)

        if position != -1:

            context = {
                "main_string": main_string,
                "sub_string": sub_string,
                "message": "Substring is present",
                "position": position
            }

        else:

            context = {
                "main_string": main_string,
                "sub_string": sub_string,
                "message": "Substring is not present",
                "position": position
            }

    return render(request, 'index.html', context)