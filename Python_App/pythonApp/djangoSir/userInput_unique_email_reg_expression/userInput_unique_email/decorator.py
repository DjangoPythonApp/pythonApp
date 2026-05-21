from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .data import context
import re
def deco_fun(home:object)->object:

    def wrapper(request:HttpRequest) -> HttpResponse:
        fname:str=''
        lname:str=''
        age:str=''
        email:str=''
        inner_context = {}
        error:str=''
        error2:str=''
        error3:str=''
        error4:str=''
        error5:str=''
        error6:str=''
        error7:str=''

        if request.method == 'POST':

            fname:str = request.POST.get('fname')

            if fname == '':
                error:str = 'Invalid first name..'
                inner_context={"error":error,
                "users":context["users"]}
                return render(request,'home.html',inner_context)

            lname:str = request.POST.get('lname')

            if lname == '':
                error2:str = 'Invalid last name..'
                inner_context={"error2":error2,
                "users":context["users"]}
                return render(request,'home.html',inner_context)

            age:str = request.POST.get('age')

            if age == '':
                error3:str = 'Invalid age..'
                inner_context={"error3":error3,
                "users":context["users"]}
                return render(request,'home.html',inner_context)

            email:str = request.POST.get('email')


            pattern = r"^[\w]+@([\w]+\.)[\w]{2,4}$"
            print(email)

            if not re.fullmatch(pattern,email):

                error4:str = 'email is not valid..'
                inner_context = {
                    "error4":error4,
                    "users":context["users"]

                }
                return render(request,'home.html',inner_context)


            for v, k in context.items():

                for user in k:
                    if user['email'] == email:
                        error7:str = 'email is already exist..'
                        inner_context={
                            "error7":error7,
                            "users":context["users"]
                            }
                        print(context)
                        return render(request,'home.html',inner_context)


        return home(request,fname,lname,age,email)

    return wrapper
