from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
import logging
from .decorator import deco_fun

logging.basicConfig(

    filename='log_file',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'

)

@deco_fun
def index(request:HttpRequest,num1,num2) -> HttpResponse:

    print(num1,num2)
    total:int = 0


    if request.method == 'POST':


    
            total:int = int(num1) + int(num2)
            logging.info(f"sum calculated {num1} + {num2} = {total}")
        



    return render(request, 'index.html',{"total":total})
    

