from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def home(request:HttpRequest)->HttpResponse:
    if request.method == "POST":
        fname:str = request.POST.get("fname")
        action = request.POST.get("action")
        # Empty Check
        if fname == "":
            context:dict = {
                "fname_error": "Empty value"
            }
            return render(request, "home/home.html", context)
        # Prime Check
        elif action == "prime":
            fname = int(fname)
            if fname<2:
                context:dict = {
                    "message": "Not Prime"
                }
                return render(request, "home/home.html", context)
            else:
                for i in range(2,fname):
                    if fname%i==0:
                        context:dict = {
                            "message": "Not Prime"
                        }
                        return render(request, "home/home.html", context)
            context:dict = {
                "message": "Prime"
            }
            return render(request, "home/home.html", context)
        # Palindrome
        elif action == "palindrome":
            fname = int(fname)
            temp:int = fname
            rem=0
            rev=0
            while(fname > 0):
                rem=fname%10
                rev=(rev*10)+rem
                fname//=10
            if rev==temp:
                context:dict = {
                    "message": "Palindrome"
                }
            else:
                context:dict = {
                    "message": "Not Palindrome"
                }
            return render(request, "home/home.html", context)
        # Reverse
        elif action == "reverse":
            fname=int(fname)
            rem=0
            rev=0
            while(fname>0):
                rem=fname%10
                rev=(rev*10)+rem
                fname//=10
            context:dict = {
                "message": f"Reverse: {rev}"
            }
            return render(request, "home/home.html", context)
        # Fibonacci
        elif action == "fibonacci":
            fib_series:list = []
            fname = int(fname)
            a:int = 0
            b:int = 1
            if fname>=1:
                fib_series.append(a)
            if fname>=2:
                fib_series.append(b)
            for i in range(2,fname):
                nextTerm:int = a + b
                fib_series.append(nextTerm)
                a:int = b
                b:int = nextTerm
                context:dict = {
                    "message": f"Fibonacci series: {fib_series}"
                }
            return render(request, "home/home.html", context)  
        # Leap Year
        elif action == "leapyear":
            fname:int = int(fname)
            if fname % 400 == 0:
                context:dict = {
                    "message": "Leap year"
                }
            elif fname%4==0 and fname%100!=0:
                context:dict = {
                    "message": "Leap year"
                }
            else:
                context:dict = {
                    "message": "Not Leap year"
                }
            return render(request, "home/home.html", context)
        # Swap No
        elif action == "swapno":
            fname:int = int(fname)
            a:int = fname // 10
            b:int = fname % 10
            swapped:int = (b*10)+a
            context:dict = {
                    "message": f"Swapped No: {swapped}"
                }
            return render(request, "home/home.html", context)

    return render(request, "home/home.html")