from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request : HttpRequest):
    context ={}
    if request.method == "POST":
        username = request.POST.get("username")
        
        context={
            "username": username}

        url = "/result/?username={}".format(username)
        # url = f'/result/?username={username}'

        return redirect(url)

        
    return render(request, "index.html", context)


def result(request : HttpRequest):
    username = request.GET.get("username")
    context = {"username": username}
    return render(request, "result.html", context)


