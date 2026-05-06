from django.shortcuts import render,  HttpResponse
import re
def index(request: HttpRequest):

    
    error=''
    success=''
    error2=''

    if request.method == 'POST':
        username = request.POST.get('username')
        if username == '':
            error = 'Username is required'

        else:
            pattern : str = r'\d'

            if re.match(pattern, username):
                success = 'String is valid'
            else:
                error2 = 'String is not valid'

    context = {
        'error': error,
        'success': success,
        'error2': error2
    }

            


    return render(request, 'index.html', context)