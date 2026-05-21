from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .decorator import deco_fun
from .data import context, context2
import random
pos = 1


@deco_fun
def home(request: HttpRequest, fname, lname, age, email) -> HttpResponse:

    global pos

    if request.method == 'POST':

        

     masked_email = ''
     masked_username = ''
 
     if email:
 
         domain = email.split('@')[1]
 
        
         for ch in email:
         
             # Randomly decide visible or masked
             if random.choice([True, False]):
                 masked_username += ch
             else:
                 masked_username += '*'
         
         masked_email = masked_username + '@' + domain
         
         
         user_data = {
             "pos": pos,
             "fname": fname,
             "lname": lname,
             "age": age,
             "email": email
         }

         context["users"].append(user_data)

         user_data2 = {
             "pos": pos,
             "fname": fname,
             "lname": lname,
             "age": age,
             "email": masked_email
         }
 
 
         context2["users"].append(user_data2)
 
         pos += 1
 
         print(context)

    return render(request, 'home.html', context2)