import logging
import re
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


logging.basicConfig(
    filename='log_file',
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s "
)

def deco_fun(index:object) -> object:

    def wrapper(request:HttpRequest) -> object:

        num1:str=''
        num2:str=''

        try:
    
            if request.method == 'POST':
    
                pattern = r'^\d{2}$'
    
                num1:str = request.POST.get('num1')
    
                if not re.match(pattern, num1):
                    logging.error(f"first value pattern does not match..")
                    raise ValueError('pattern not match..')
                    
    
                num2:str = request.POST.get('num2')
    
                if not re.match(pattern, num2):
                    logging.error(f"fsecond value pattern does not match..")
                    raise ValueError('pattern not match..')
    
    
                
                logging.info(f"two values are succesfully validat...")
    
            
    
            return index(request,num1,num2)
    
    
        except ValueError as e:
    
            return render(request, 'index.html',{"error1":str(e)})
    
        except Exception as e:
            return render(request, "index.html", {"error":str(e)})


    return wrapper

