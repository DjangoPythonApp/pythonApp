from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from .decorator import email_validator


@email_validator
def index(request: HttpRequest)->HttpResponse:

    context = {}
    email=''
    username=''
    error:str=""

    if request.method == "POST":

        email = request.POST.get('email')
        sentence = request.POST.get('sentence')
        

        # Extract username from email
        username = email.split('@')[0]

        

        context = {
            'email': email,
            'username': username,
            'error':error
            
        }

    return render(request, 'index.html', context)