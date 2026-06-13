from django.shortcuts import render,redirect,get_object_or_404
from .models import Person

def person_list(request):
    persons=Person.objects.all()
    return render(request,'person_list.html',{'persons':persons})

def person_create(request):
    if request.method=="POST":
        Person.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            address=request.POST['address'],
            course_enrolled=request.POST['course_enrolled'],
            image=request.FILES['image']
        )
        return redirect('person_list')
    return render(request,'person_form.html')

def person_update(request,pk):
    person=get_object_or_404(Person,id=pk)
    if request.method=="POST":
        person.name=request.POST['name']
        person.age=request.POST['age']
        person.address=request.POST['address']
        person.course_enrolled=request.POST['course_enrolled']
        if 'image' in request.FILES:
            person.image=request.FILES['image']
        person.save()
        return redirect('person_list')
    return render(request,'person_form.html',{'person':person})

def person_delete(request,pk):
    person=get_object_or_404(Person,id=pk)
    person.delete()
    return redirect('person_list')
