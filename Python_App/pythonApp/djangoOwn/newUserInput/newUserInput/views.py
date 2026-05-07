
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

item_list:list =[]
pos : int = 0

def index(request: HttpRequest):

    context: dict = dict()
    global pos

    if request.method == 'POST':
        fname  = request.POST.get('fname')
        lname  = request.POST.get('lname')
        age    = request.POST.get('age')

        if fname and lname and age:

            item_list.append((fname,lname,age))
            context ={

                "items": item_list

            }  

        else:
            context['message'] = 'Please enter the valid data.'
    
    if len(item_list) > 0:

        context ={

                "items": item_list,
                "message": message

            }
    print(context)
    return render(request,'index.html',context)

    

