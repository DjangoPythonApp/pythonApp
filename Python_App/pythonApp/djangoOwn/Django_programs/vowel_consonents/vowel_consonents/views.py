from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:

    context = {}
    message=''
    v1= 0
    c1= 0
    vow = ''
    con = ''
    data = ''
    print('Hello') 

    if request.method == 'POST':
        print("hello")

        if request.POST == '':
            message:str = 'Please enter the data!!'
            context = {
                'message':message
            }
            return render(request,'index.html',context)

        data:str = request.POST.get("data")
        print(data)
        


        data2:str = ",".join(data)
        print(data2)
        arr:list =[]

        for i in data2:
            low=i.lower()
            arr.append(low)

        print(arr)

        vowel = ['a','e','i','o','u']
        consonent = [
        'b','c','d','f','g','h','j','k','l','m',
        'n','p','q','r','s','t','v','w','x','y','z']

       

        for i in arr:
            if i in vowel:
                v1+=1

      
        vow=f'The number of vowels:{v1}'

        for i in arr:
            if i in consonent:
                c1+=1

        
        con=f'The number of consonent:{c1}'

    context = {
        'data':data,
        'v1':vow,
        'c1':con,
        'message':message
    }
    print(v1,c1)


    return render(request, 'index.html',context)