from django.shortcuts import render


def index(request):
    context = {}
    print("Hello world")
    print(request.method)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        if fname and lname:
            context ={
                "fname": fname,
                "lname": lname
            }

        else:
            context = {
                "error": "Please provide both first name and last name."
            }

        
 
    
        

    
    return render(request, "index.html",context)