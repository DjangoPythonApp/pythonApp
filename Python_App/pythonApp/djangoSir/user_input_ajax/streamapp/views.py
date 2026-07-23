from django.shortcuts import render
from django.http import HttpRequest, JsonResponse

def home(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'index.html')


def addStream(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'stream/add.html')
        
    if request.method == 'POST':        
        firstNum: int = int(request.POST.get('firstNum'))
        secondNum: int = int(request.POST.get('secondNum'))
        result: int = firstNum + secondNum

        return JsonResponse({
            'result': result, 
            'firstNum': firstNum,
            'secondNum': secondNum}
        )
