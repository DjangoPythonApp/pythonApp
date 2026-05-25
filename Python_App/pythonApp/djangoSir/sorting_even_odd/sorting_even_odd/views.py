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



        for i in range(len(context['even'])-1):

            for j in range(len(context['even'])-i-1):

                if context['even'][j] > context['even'][j+1]:
                    temp:int = context['even'][j]
                    context['even'][j] = context['even'][j+1]
                    context['even'][j+1] = temp

        


        for i in range(len(context['odd']) - 1 ):

            for j in range(len(context['odd'])-i-1):

                if context['odd'][j] > context['odd'][j+1]:
                    temp:int = context['odd'][j]
                    context['odd'][j] = context['odd'][j+1]
                    context['odd'][j+1] = temp

        print(context['even'])

      
        print(context['odd'])



    return render(request, 'index.html',context)