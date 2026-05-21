# decorators.py

from django.shortcuts import render
from django.http import HttpRequest

def mask_email(func_view: object) -> object:

    def wrapper(request: HttpRequest) -> object:
        if request.method == 'POST':
            email = request.POST.get('email')
            if email and '@' in email:
                request.new_email = email.split('@')[0]                         # Add the new_email attribute inside the request
                return func_view(request)
            else:
                context = {
                    'error': 'Invalid email address'
                }
                return render(request, "index/index.html", context)
        return func_view(request)
    
    return wrapper