from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .decorator import deco_fun
from .data import context
pos = 1


@deco_fun
def home(request: HttpRequest, fname, lname, age, email) -> HttpResponse:

    global pos

    if request.method == 'POST':

        user_data = {
            "pos": pos,
            "fname": fname,
            "lname": lname,
            "age": age,
            "email": email
        }

        

        context["users"].append(user_data)

        pos += 1

        print(context)

    return render(request, 'home.html', context)