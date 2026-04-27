from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

items_list: list = []
pos: int = 0
status: bool = True

def home(request:HttpRequest):              # Function Based View
    # context = {}            # Initialize context as a dictionary
    context = dict()
    print(type(context))
    global pos

    if request.method == 'POST':
        fname = request.POST.get('fname')           # This will fetch the data from DOM element having attibute name="fname"
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        pos+=1
        if age and fname and lname:
            # context['fname'] = fname
            # context['lname'] = lname
            # context['age'] = age
            
            items_list.append((pos, fname, lname, age))  # Store as a tuple
            context = {
                'items': items_list  # Pass the list of tuples to the template
            }
        else:
            context['message'] = "Empty value not allowed"
    
    if len(items_list) > 0:
        context = {
            'items': items_list  # Pass the list of tuples to the template
        }
    return render(request, "home/index.html", context)

def edit_view(request: HttpRequest, item_id):
    item = None
    for i in range(len(items_list)):
        if items_list[i][0] == item_id:
            item = items_list[i]
            break

    if not item:
        return HttpResponse("Item not found", status=404)

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')

        # Update the item in the items_list
        updated_item = (item_id, fname, lname, age)
        items_list[i] = updated_item
        context = {
            'items': items_list  # Pass the list of tuples to the template
        }

        return redirect('home')  # Assuming 'home' is your list page
        # return render(request, "home/index.html", context)

    # Pass the current item data to the template for editing
    context = {
        'item': item
    }
    return render(request, 'home/edit_item.html', context)

def delete_view(request, item_id):
    global items_list
    items_list = [item for item in items_list if item[0] != item_id]
    return redirect('home') 


# def home(request):
#     # context = {}            # Initialize context as a dictionary
#     context = dict()
#     print(type(context))

#     if request.method == 'POST':
#         age = request.POST.get('age')
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')

#         if age and fname and lname:
#             context['age'] = age
#             context['fname'] = fname
#             context['lname'] = lname
#             context['message'] = f"Age: {age} Name: {fname} {lname}"
#         else:
#             context['message'] = "Empty value not allowed"
#     return render(request, "home/index.html", context)
    # return HttpResponse(f"Age: {age} Name: {fname} {lname}")