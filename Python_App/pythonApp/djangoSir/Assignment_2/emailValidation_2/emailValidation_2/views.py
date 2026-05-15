from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random
from .decorator import deco_fun


@deco_fun
def index(request:HttpRequest,username,email)->HttpResponse:


    masked_email = ''
    masked_username = ''

    if email:

        domain = email.split('@')[1]

       
        for ch in username:
        
            # Randomly decide visible or masked
            if random.choice([True, False]):
                masked_username += ch
            else:
                masked_username += '*'
        
        masked_email = masked_username + '@' + domain
        

    context = {

        "username": username,
        "email": masked_email
    }






    return render(request, 'index.html',context)