from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Insert
# Create your views here.
def index(request:HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def create(request:HttpRequest) -> HttpResponse:

    if request.method == 'POST':

        name:str = request.POST.get('name')
        age:str = request.POST.get('age')

        Insert.objects.create(name=name, age=age)
        
        return redirect('display_list')
        

    
    return render(request, 'insert.html')



    
def read(request:HttpRequest) -> HttpResponse:
   data =  Insert.objects.all()
   return render(request,"display_list.html" ,{"data":data})



def edit(request:HttpRequest,id) -> HttpResponse:
    
    data = Insert.objects.get(id=id)

    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.age = request.POST.get('age')
        data.save()

        return redirect('display_list')
    
    return render(request, 'edit_page.html',{"data":data})



def delete(request: HttpRequest, id) -> HttpResponse:

    data = Insert.objects.get(id=id)
    print("Data",data)
    print(type(data))
    data.delete()

    return redirect('display_list')
