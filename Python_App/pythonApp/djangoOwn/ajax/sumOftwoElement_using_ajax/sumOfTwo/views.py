from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
# Create your views here.
def addition(request: HttpRequest) -> HttpResponse:
    result = None
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        result = num1 + num2
        return JsonResponse({
                             'num1': num1,
                             'num2': num2,
                             'sum': result  })
        return render(request, 'add.html', {'result': result})
    return render(request, 'add.html', {'result': result})