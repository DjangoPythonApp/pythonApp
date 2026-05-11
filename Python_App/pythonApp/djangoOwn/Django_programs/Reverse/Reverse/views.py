from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def reverse(request: HttpRequest) -> HttpResponse:

    context={}
    error:str=''
    number:int = 0

    if request.method == 'POST':

        num = request.POST.get('num')

        if num == '':
            error:str="Please enter the value!!!"
            return render(request,'index.html',context={ "error" : error})


        else:

            new_num = int(num)
            rem=0
            sum1=0
            x=new_num

            while x!=0:
                rem = x % 10
                sum1 = sum1 * 10 + rem 
                x = x // 10

            number = sum1

            context ={
                'number':number
            }

    print(context)
    return render(request, 'index.html',context)

            