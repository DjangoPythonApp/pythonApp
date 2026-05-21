from django.shortcuts import render
from django.http import HttpRequest

from .decorators import mask_email
import random

@mask_email
def home(request: HttpRequest):
    if request.method == 'POST':
        # email = request.POST.get('email')

        if email:
            domain = email.split('@')[1]
            user_name = ""

            for char in request.new_email:
                choice = random.randint(0, 1)
                if choice == 0:
                    user_name += '*'
                else:
                    user_name += char

            masked_email = user_name + '@' + domain
            context = {
                'masked_email': masked_email
            }
            return render(request, "index/index.html", context)
    return render(request, "index/index.html")