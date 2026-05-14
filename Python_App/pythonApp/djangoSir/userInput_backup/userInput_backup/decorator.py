from django.shortcuts import render

def validate_number(view_func:object)->object:

    def wrapper(request, item_id, *args, **kwargs):

        from .views import items_list,backUp_list

        

        for item in items_list:

            if item[0] == item_id:

                backUp_list.append(item)

        print(backUp_list)

        return view_func(request, item_id, *args, **kwargs)

    return wrapper