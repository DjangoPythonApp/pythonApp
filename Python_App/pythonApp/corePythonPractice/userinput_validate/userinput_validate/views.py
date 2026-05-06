from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

def home(request:HttpRequest):

    message:str = ""
    fname_error = ""
    lname_error = ""

    if request.method == "POST":
        fname:str = request.POST.get("fname")
        lname:str = request.POST.get("lname")

        if fname=="":
            fname_error:str = "First name is required"

        if lname=="":
            lname_error:str = "Last name is required"
    
        if fname !="" and lname !="":
            message:str = f"Welcome {fname} {lname} to the world of Python"

    context = {
        "message": message,
        "fname_error": fname_error,
        "lname_error": lname_error,
    }

    return render(request, "home/home.html", context)














