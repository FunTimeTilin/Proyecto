from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import bcchapi
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

# Create your views here.

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Usuario creado'
            return redirect('login')
        else:
            msg = 'Formulario invalido'
    else:
        form = SignUpForm()
    return render(request, 'ferremapp/register.html', {'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('index')
            elif user is not None and user.is_vendedor:
                login(request, user)
                return redirect('vendedor')
            elif user is not None and user.is_bodeguero:
                login(request, user)
                return redirect('bodeguero')
            elif user is not None and user.is_contador:
                login(request, user)
                return redirect('contador')
            elif user is not None and user.is_cliente:
                login(request, user)
                return redirect('cliente')
            else:
                msg = 'Credenciales invalidas'
        else:
            msg = 'Error al enviar el formulario'
    return render(request, 'ferremapp/login.html', {'form': form, 'msg': msg})

@login_required
def index(request):
    return render(request, 'ferremapp/index.html')
@login_required
def vendedor(request):
    return render(request, 'ferremapp/vendedor.html')
@login_required
def bodeguero(request):
    return render(request, 'ferremapp/bodeguero.html')
@login_required
def contador(request):
    return render(request, 'ferremapp/contador.html')
@login_required
def cliente(request):
    return render(request, 'ferremapp/cliente.html')
@login_required
def carrito(request):
    return render(request, 'ferremapp/carrito.html')
@login_required
def catalogo(request):
    return render(request, 'ferremapp/catalogo.html')
@login_required
def epp(request):
    return render(request, 'ferremapp/EPP.html')
@login_required
def herramientasmanuales(request):
    return render(request, 'ferremapp/herramientas_manuales.html')
@login_required
def materialesligeros(request):
    return render(request, 'ferremapp/materiales_ligeros.html')
@login_required
def pint_ext(request):
    return render(request, 'ferremapp/pint_ext.html')
@login_required
def piso_flotante(request):
    return render(request, 'ferremapp/Piso_flot.html')
@login_required
def acercade(request):
    return render(request, 'ferremapp/acercade.html')
@login_required
def contacto(request):
    return render(request, 'ferremapp/contacto.html')

def buscarSeries(request):
    if request.method == 'POST':
        termino_busqueda = request.POST['termino']
        siete = bcchapi.Siete(file="credenciales.txt")
        resultados_df = siete.buscar(termino_busqueda)
        # Convertir el DataFrame en una lista de diccionarios
        resultados = resultados_df.to_dict('records')
        return render(request, 'ferremapp/resultados.html', {'resultados': resultados})
    else:
        return render(request, 'ferremapp/buscar.html')


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer