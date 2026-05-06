from django.shortcuts import render, HttpResponse, HttpResponseRedirect



def fuzzy_support(request):
    context = {}

    if request.method == "POST":
        n = int(request.POST.get("num"))

        fuzzy = {}
        support = []

        for i in range(n):
            element = request.POST.get(f"e{i}")
            membership = request.POST.get(f"m{i}")

            if element and membership:
                m = float(membership)
                fuzzy[element] = m

                if m > 0:
                    support.append(element)

        context["n"] = n
        context["fuzzy"] = fuzzy
        context["support"] = support

    return render(request, "crispy.html", context)