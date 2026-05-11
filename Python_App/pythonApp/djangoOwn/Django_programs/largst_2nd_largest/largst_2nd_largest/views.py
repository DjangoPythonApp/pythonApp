from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:

    context = {}
    arr = []

    if request.method == 'POST':

        # FIRST FORM
        if request.POST.get('no') and not request.POST.get('number_0'):

            no = int(request.POST.get('no'))

            context = {
                'no': no
            }

            return render(request, 'index.html', context)

        # SECOND FORM
        no = int(request.POST.get('no'))

        # Store array elements
        for i in range(no):

            data = request.POST.get(f"number_{i}")

            if data:
                data = int(data)
                arr.append(data)

        # Bubble Sort
        le = len(arr)

        for i in range(le - 1):

            for j in range(le - i - 1):

                if arr[j] > arr[j + 1]:

                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp

        print(arr)

        maax = arr[le - 1]
        secondMax = arr[le - 2]

        context = {
            'largest': maax,
            'second_largest': secondMax,
            'no': no
        }

    return render(request, 'index.html', context)