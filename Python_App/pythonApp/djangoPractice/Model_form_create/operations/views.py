from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.


# def index(request:HttpRequest) -> HttpResponse:
#     return render(request, 'index.html')


def student_create_view(request:HtppRequest) -> HttpResponse:
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        

        if form.is_valid():
            form.save()
            return render(request, 'submit.html')

    else:

        form = StudentForm() # Clear the form after saving

    return render(request, 'form.html', {'form':form})


def submit_view(request):
    return render(request, 'submit.html')


def student_list(request:HttpRequest) -> HttpResponse:
    students = Student.objects.all()
    return render(request, 'student_list',{'students':students})


def student_details(request:HttpRequest,pk) -> HttpResponse:
    
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html',{'student':student})
