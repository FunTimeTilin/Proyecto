from django.shortcuts import render

# Create your views here.
def menu(request):
    context = {}
    return render (request, "pages/menu.html", context)
def EPP(request):
    context = {}
    return render (request, "pages/EPP.html", context)