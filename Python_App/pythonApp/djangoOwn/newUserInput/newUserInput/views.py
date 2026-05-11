
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

item_list:list =[]
pos : int = 0
message : str = ''
def index(request: HttpRequest):
    

    context: dict = dict()
    global pos

    if request.method == 'POST':
        fname  = request.POST.get('fname')
        lname  = request.POST.get('lname')
        age    = request.POST.get('age')
        pos+=1

        if fname and lname and age:

            item_list.append([pos,fname,lname,age])
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

    

def edit_view(request: HttpRequest, item_id):

    item = None
    for i in range(len(item_list)):
        if item_list[i][0] == item_id:
            item = item_list[i]
            break

    else:
        return HttpResponse("Item not found!!",status=404)

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        update_list = [item_id,fname,lname,age]

        item_list[i] = update_list

        context = {
            
            'items': item_list
        }

        return redirect('index')


    context = {

        'item': item
    }

    print(context)

    return render(request, 'edit.html',context)

    





def delete_view(request: HttpRequest,item_id):
    
    global item_list

    new_list = []

    for item in item_list:
        if item[0] != item_id:
            print(item[0])
            new_list.append(item)

    for i in range(len(new_list)):
        new_list[i][0] = i + 1

    item_list = new_list

    return redirect('index')

    
