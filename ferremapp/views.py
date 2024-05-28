from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import bcchapi
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer
from django.http import JsonResponse
from django.conf import settings
from django.urls import reverse
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions
from transbank.common.integration_type import IntegrationType


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

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def index(request):
    return render(request, 'ferremapp/index.html')
@login_required
def vendedor(request):
    Productos = Producto.objects.all()
    return render(request, 'ferremapp/vendedor.html', {'Productos': Productos})
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

def obtener_producto(request, codigo_producto):
    producto = Producto.objects.filter(codigo_producto=codigo_producto)
    if producto:
        return JsonResponse({
            'marca': producto.marca,
            'codigo': producto.codigo,
            'nombre': producto.nombre,
            'fecha': producto.fecha,
            'valor': producto.valor
        })
    else:
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

def antiparra(request):
    return render(request, 'ferremapp/antiparra.html')

def guantes(request):
    return render(request, 'ferremapp/guantes.html')

def protectoroido(request):
    return render(request, 'ferremapp/protector_oido.html')

def mascara(request):
    return render(request, 'ferremapp/mascara.html')

def zapatoseguridad(request):
    return render(request, 'ferremapp/zapato_seguridad.html')

def initiate_payment(request):
    transaction = Transaction(WebpayOptions(
        commerce_code='597055555532',             # Test commerce code
        api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
        integration_type=IntegrationType.TEST     # Use TEST for sandbox
    ))
    response = transaction.create(
        buy_order='order123456789',
        session_id='session123456',
        amount=100000,                              # Amount in CLP
        return_url=request.build_absolute_uri(reverse('payment_confirm'))
    )
    return redirect(response['url'] + '?token_ws=' + response['token'])

def payment_confirm(request):
    token = request.GET.get('token_ws')
    transaction = Transaction(WebpayOptions(
        commerce_code='597055555532',             # Test commerce code
        api_key='579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C',
        integration_type=IntegrationType.TEST     # Use TEST for sandbox
    ))
    response = transaction.commit(token)

    if response['status'] == 'AUTHORIZED':
        return render(request, 'ferremapp/approved.html', {'response': response})
    else:
        return render(request, 'ferremapp/failed.html', {'response': response})