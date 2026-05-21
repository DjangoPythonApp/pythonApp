from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .decorator import deco_fun
from .data import context

pos:int = 1

@deco_fun
def index(request:HttpRequest,fullName,marks) -> HttpResponse:


    inner_dict:dict ={}

    if request.method == 'POST':

        global pos
        print("Full Name:",fullName)
        print("Marks:",marks)
    
        arr:list = list(map(int, marks.split()))
    
        sum1:int = 0
        
        for i in arr:
            sum1+=i
    
        avg:int = sum1//len(arr)
    
        grade:str=''
    
        print('Total:',sum1)
        print('AVG:',avg)
    
        if avg <=100 and avg >70:
    
            grade:str = 'A'
    
        elif avg <=70 and avg >50:
    
            grade:str = 'B'
    
        elif avg <=50 and avg >30:
    
            grade:str = 'C'
    
        else:
    
            grade:str = 'Fail'
    
    
        inner_dict:dict = {'id':pos,"fullName":fullName,'marks':sum1,'average':avg,'grade':grade}
        pos+=1
    
        context['data'].append(inner_dict)
    
        print(context)


    return render(request, 'index.html',context)