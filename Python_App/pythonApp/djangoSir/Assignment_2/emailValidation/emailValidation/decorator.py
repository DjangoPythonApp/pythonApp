from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def email_validator(myFunction):

    def inner(request: HttpRequest):



        if request.method == "POST":

            

             email = request.POST.get('email')

             if email == '':

                error:str = 'Enter the email..'

                context = {
                     "error":error
                 }
     
                return render(request, 'index.html', context)
     

     
             # Check whether email contains '@'
             if '@' not in email:
                 error:str = 'Invalid email because @ not found!!!'
     
                 context = {
                     "error":error
                 }
     
                 return render(request, 'index.html', context)
     
             # Check whether email ends with '.com'
             if not email.endswith('.com'):
                  error:str = "Invalid Email! Email must end with .com"
     
                  context = {
                     "error":error
                 }
     
                  return render(request, 'index.html', context)
     
             # If valid
        return myFunction(request)

    return inner