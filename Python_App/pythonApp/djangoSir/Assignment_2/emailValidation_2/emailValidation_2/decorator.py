from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def deco_fun(index:object) -> object:

    def wrapper(request: HttpRequest)->HttpResponse:

        username = ''
        email =''

        if request.method == 'POST':
            email = request.POST.get('email')

            if email == '':

                error = 'Enter the email..'

                context = {
                    "error": error
                }

                return render(request, 'index.html', context)

            if '@' not in email:

                error = 'Invalid email because @ not found!!!'

                context = {
                    "error": error
                }

                return render(request, 'index.html', context)

            if not email.endswith('.com'):

                error = "Invalid Email! Email must end with .com"

                context = {
                    "error": error
                }

                return render(request, 'index.html', context)

    


            username = email.split('@')[0]

        return index(request, username,email)

    return wrapper