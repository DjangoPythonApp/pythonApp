from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

item_list:list = []
pos:int = 0
status:bool = True

def index(request:HttpRequest):

    context:dict = {}
    global pos

    if request.method == 'POST':

        name:str = request.POST.get('name')
        age:str = request.POST.get('age')
        email:str = request.POST.get('email')
        pos+=1

        if name and age and email:

            item_list=[[pos,name,age,email]]


            item_list.append([pos,name,age,email])
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



    