from django.shortcuts import render

def home(request):
    context = {}

    if request.method == 'POST':
        first = request.POST.get('first_name', '').strip()
        last = request.POST.get('last_name', '').strip()

        if not first:
            context['first_error'] = "Provide your first name"

        if not last:
            context['last_error'] = "Provide your last name"

        if first and last:
            context['name'] = f"{first} {last}"

    return render(request, 'home.html', context)