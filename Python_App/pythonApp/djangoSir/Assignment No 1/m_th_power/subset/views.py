from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:

    context: dict = {}
    message: str = ''

    if request.method == 'POST':

        n = request.POST.get('num', 0)
      

        print(n)

        n = int(n)
       

        print("value of N:", n)

      

        dict_A: dict = dict()

        print('set A:')

        for i in range(n):

            ele = request.POST.get(f"ae{i}")
            membership = request.POST.get(f"am{i}")

            if ele and membership:

                membership = float(membership)

                dict_A.update({ele: membership})

        print(dict_A)

      
        dict_B:dict ={}

        power_set:dict = {k: round(v ** 2, 2) for k, v in dict_A.items()}

        print(power_set)

    
       



        context = {

            "n": n,
            "dict_A":dict_A,
            "dict_B":power_set
        }

        return render(request, 'index.html', context)

    return render(request, 'index.html')