from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .decorator import deco_fun
from .data import context
@deco_fun
def index(request:HttpRequest,data) ->HttpResponse:

    if request.method == 'POST':

        arr:list = list(map(int, data.split()))

        context['mainList'] = arr

        print(context['mainList'])

        for i in arr:

            if i%2 == 0:

                context['even'].append(i)

            else:

                context['odd'].append(i)



    return render(request, 'index.html',context)