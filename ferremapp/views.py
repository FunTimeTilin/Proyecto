from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    return render(request, 'ferremapp/index.html')

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

def vendedor(request):
    return render(request, 'ferremapp/vendedor.html')

def bodeguero(request):
    return render(request, 'ferremapp/bodeguero.html')

def contador(request):
    return render(request, 'ferremapp/contador.html')

def cliente(request):
    return render(request, 'ferremapp/cliente.html')

def carrito(request):
    return render(request, 'ferremapp/carrito.html')

def catalogo(request):
    return render(request, 'ferremapp/catalogo.html')

def epp(request):
    return render(request, 'ferremapp/EPP.html')

def herramientasmanuales(request):
    return render(request, 'ferremapp/herramientas_manuales.html')

def materialesligeros(request):
    return render(request, 'ferremapp/materiales_ligeros.html')

def pint_ext(request):
    return render(request, 'ferremapp/pint_ext.html')

def piso_flotante(request):
    return render(request, 'ferremapp/Piso_flot.html')

def acercade(request):
    return render(request, 'ferremapp/acercade.html')

def contacto(request):
    return render(request, 'ferremapp/contacto.html')