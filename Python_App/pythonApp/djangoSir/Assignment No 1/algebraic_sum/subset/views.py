from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:

    context: dict = {}
    message: str = ''

    if request.method == 'POST':

        n = request.POST.get('num', 0)
        n2 = request.POST.get('num2', 0)

        print(n, n2)

        n = int(n)
        n2 = int(n2)

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

      

        dict_B: dict = dict()

        print('set B:')

        for i in range(n2):

            ele = request.POST.get(f"be{i}")
            membership = request.POST.get(f"bm{i}")

            if ele and membership:

                membership = float(membership)

                dict_B.update({ele: membership})

        print(dict_B)

       

        algebraicSum:dict = dict()
        for k, v in  dict_A.items():
            algebraicSum.update({k:round(v+dict_B[k] - v*dict_B[k],2)})

        print(algebraicSum)
                
                
                
                
       
       


       
        context = {
            "n":n,
            "n2":n2,
            "dict_A":dict_A,
            "dict_B":dict_B,
            "dict_C":algebraicSum
        }

        return render(request, 'index.html', context)

    return render(request, 'index.html')