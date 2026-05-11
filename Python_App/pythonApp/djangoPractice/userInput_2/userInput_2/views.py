from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

item_list = []
pos:int = 0
status:bool = True

def index(request : HttpRequest):

    global pos
    context = {}
    message=''

    if request.method == 'POST':
        name:str = request.POST.get('name')
        age:str = request.POST.get('age')
        email:str = request.POST.get('email')
        

        print(name,age,email)

        if name and age and  email:

            pos+=1
            
            item_list.append([pos,name,age,email])

        else:

            message:str = 'Please enter the data.'
            
            


    context = {
        "item_list":item_list,
        "message":message
    }
    print(context)
    return render(request,'index.html',context)


def edit(request:HttpRequest, item_id):
    item=None
    print(type(item_id))
    for i in range(len(item_list)):
        if item_list[i][0] == item_id:
            item = item_list[i]
            break

    else:
        return HttpResponse('<h2>Data not found!!!</h2>',status=404)

    print(item_list)

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        updated_list:list = [item_id,name,age,email]

        item_list[i] = updated_list
        print(item_list)

        context = {
            "item_list":item_list
        }

        return redirect('index')

    context = {
        "item":item
    }



    return render(request,'edit.html',context)


def delete(request:HttpRequest, item_id):

    global item_list

    print('item_list:',item_list)
    new_list = []

    for item in item_list:
       if item[0] != item_id:

         new_list.append(item)

    print('new_list:',new_list)

    for i in range(len(new_list)):
       new_list[i][0] = i+1

    item_list = new_list

    

    return redirect('index')