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

       
        listA = []

        for k, v in dict_A.items():

            listA.append((k, v))

        print(listA)

        listB = []

        for k, v in dict_B.items():

            listB.append((k, v))

        print(listB)

       

        if len(dict_A) != n or len(dict_B) != n2:

            message = 'Please enter all the inputs..'

        else:

           

            flag: bool = True

            for i in range(min(len(listA), len(listB))):

                if listB[i][1] < listA[i][1]:

                    flag = False
                    break

           

            if flag:

                message = 'Fuzzy set A is a subset of Fuzzy set B.'

            else:

                message = 'Fuzzy set A is not a subset of Fuzzy set B.'

        context = {

            "n": n,
            "n2": n2,
            "message": message,
        }

        return render(request, 'index.html', context)

    return render(request, 'index.html')