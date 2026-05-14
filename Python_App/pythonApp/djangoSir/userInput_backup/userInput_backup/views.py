from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .decorator import validate_number
items_list: list = []
backUp_list: list = []
pos: int = 0


def home(request:HttpRequest)->HttpResponse:
    global pos
    if request.method == 'POST':
        pname:str = request.POST.get('pname')  
        cname:str = request.POST.get('cname')
        price = request.POST.get('price')

        if price and pname and cname:
            pos+=1
            
            items_list.append((pos, pname, cname, price)) 
            context = {
                'items': items_list,
                'message': 'Product added successfully'
            }
            return render(request, "home/index.html", context)
        else:
            context = {
                'items': items_list,  
                'message': 'Empty value not allowed'
            }
            # context['message'] = "Empty value not allowed"  
        return render(request, "home/index.html", context)
    return render(request, "home/index.html")

@validate_number
def delete_view(request, item_id):
    global items_list
    items_list = [item for item in items_list if item[0] != item_id]
    return redirect('home') 