from django.http import JsonResponse
from .models import Category


def prevent_duplicate_category(view_function):

    def wrapper(request, *args, **kwargs):
        if request.method == "POST":
            category_id = request.POST.get('category_id')
            name = request.POST.get('name')
            
            if not category_id:
                if Category.objects.filter(name=name).exists():
                    return JsonResponse({
                        'success': False,
                        'message': 'Category already exists'
                    })
            else:
                if Category.objects.filter(name=name)\
                                   .exclude(id=category_id)\
                                   .exists():

                    return JsonResponse({
                        'success': False,
                        'message': 'Category already exists'
                    })
        return view_function(request, *args, **kwargs)

    return wrapper