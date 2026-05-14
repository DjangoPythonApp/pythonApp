from django.shortcuts import render

def validate_number(view_func):

    def wrapper(request):

        from .views import item_list

        if request.method == 'POST':

            email = request.POST.get('email')

            for item in item_list:

                if item[3] == email:

                    context = {
                        "item_list": item_list,
                        "message": "Email already exists"
                    }

                    return render(request, 'index.html', context)

        return view_func(request)

    return wrapper