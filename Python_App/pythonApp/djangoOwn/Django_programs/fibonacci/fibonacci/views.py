from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse

def index(request:HttpRequest):

    context:dict=dict()
    fibo_list:list = list()
    message=''

    if request.method == 'POST':

        data:str = request.POST.get('data')

        if data == '':

            message="please insert the data."

        else:
            data2 :int = int(data)
            no1:int = 0
            no2:int = 1
            new_no:int = no1 + no2
            fibo_list = [no1,no2,new_no]
            
            

            for _ in range(data2-3):
                no1=no2
                no2=new_no
                new_no=no1+no2
                fibo_list.append(new_no)


    context ={

        "fibo_list":fibo_list,
        "message":message
    }

            


        

    return render(request,'index.html',context)