from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index(request: HttpRequest) -> HttpResponse:

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

            if new_num == sum1:
                message:str=f'{new_num} is a palindrome number.'
            else:
                message:str=f'{new_num} is not a palindrome number.'

            context ={
                'number': message
            }

    print(context)
    return render(request, 'index.html',context)

            