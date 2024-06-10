from django.shortcuts import render


# Create your views here.
def menu(request):
    context = {}
    return render (request, "pages/menu.html", context)
def EPP(request):
    context = {}
    return render (request, "pages/EPP.html", context)
def inicio_sesion (request):
    context = {}
    return render (request, "pages/inicio_sesion.html", context)
def registro(request):
    context = {}
    return render (request, "pages/registro.html", context)
def acercade(request):
    context = {}
    return render (request, "pages/acercade.html", context)
def antiparra(request):
    context = {}
    return render (request, "pages/antiparra.html", context)
def carrito(request):
    context = {}
    return render (request, "pages/carrito.html", context)
def contacto(request):
    context = {}
    return render (request, "pages/contacto.html", context)
def guantes(request):
    context = {}
    return render (request, "pages/guantes.html", context)
def herramientas(request):
    context = {}
    return render (request, "pages/herramientas.html", context)
def mascara(request):
    context = {}
    return render (request, "pages/mascara.html", context)
def materiales(request):
    context = {}
    return render (request, "pages/materiales.html", context)
def pintura(request):
    context = {}
    return render (request, "pages/pintura.html", context)
def piso(request):
    context = {}
    return render (request, "pages/piso.html", context)
def protector(request):
    context = {}
    return render (request, "pages/protector.html", context)
def zapatos(request):
    context = {}
    return render (request, "pages/zapatos.html", context)




