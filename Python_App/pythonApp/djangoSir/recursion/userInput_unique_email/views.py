from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# from .decorator import deco_fun
# from .data import context


context = {
    "data": []
}


def home(request: HttpRequest) -> HttpResponse:

  

    if request.method == 'POST':

        item:list = request.POST.get('item')

        arr:list = list(item)
        print(arr)
        




        

        

        

       

    return render(request, 'home.html', context)