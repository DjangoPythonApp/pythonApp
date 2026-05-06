from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def form(request):
    context = {}   

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        context = {
            'name': name,
            'age': age,
            'email': email
        }

    return render(request, 'form.html', context=context)


def edit(request, name, age, email):

    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")

        return redirect('form')

    context = {
        'name': name,
        'age': age,
        'email': email
    }

    return render(request, "edit.html", context)


from django.shortcuts import redirect

def delete(request):
    # Just redirect to form WITHOUT query parameters
    return redirect('form')
