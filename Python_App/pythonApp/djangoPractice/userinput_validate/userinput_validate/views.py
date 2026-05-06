from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
import re

def home(request:HttpRequest):

    message:str = ""
    fname_error = ""
    new_error = ""

    if request.method == "POST":
        fname = request.POST.get("fname")
        print(type(fname))
        pattern : str = r"ab?a"


        if fname=="":
            fname_error:str = "First name is required"

        if re.match(pattern, fname):
                message:str = f"String {fname} is matching the pattern"
        else:
                new_error:str = "String does not match the pattern"


    context = {
        "message": message,
        "new_error": new_error,
       
    }

    return render(request, "home/home.html", context)














