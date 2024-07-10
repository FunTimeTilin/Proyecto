from django.shortcuts import render
from .models import Genero, Usuario, Cargo, Producto, Categoria
from .forms import GeneroForm,UsuarioForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def menu(request):
    context = {}
    return render (request, "pages/menu.html", context)

def registro(request):
    context = {}
    return render (request, "pages/registro.html", context)

def acercade(request):
    context = {}
    return render (request, "pages/acercade.html", context)

def carrito(request):
    context = {}
    return render (request, "pages/carrito.html", context)

def contacto(request):
    context = {}
    return render (request, "pages/contacto.html", context)


""" EPP """

def EPP(request):
    context = {}
    return render (request, "pages/EPP.html", context)

def antiparra(request):
    context = {}
    return render (request, "pages/antiparra.html", context)

def mascara(request):
    context = {}
    return render (request, "pages/mascara.html", context)

def protector(request):
    context = {}
    return render (request, "pages/protector_oido.html", context)

def zapatos(request):
    context = {}
    return render (request, "pages/zapatos.html", context)

def guantes(request):
    context = {}
    return render (request, "pages/guantes.html", context)


""" MATERIALES LIGEROS """

def materiales(request):
    context = {}
    return render (request, "pages/materiales_ligeros.html", context)

def pintura(request):
    context = {}
    return render (request, "pages/pint_ext.html", context)

def piso(request):
    context = {}
    return render (request, "pages/piso_flot.html", context)

def cemento(request):
    context = {}
    return render (request, "pages/cemento.html", context)

def agorex(request):
    context = {}
    return render (request, "pages/agorex.html", context)
    
def ladrillo(request):
    context = {}
    return render (request, "pages/ladrillo.html", context)

def saco_arena(request):
    context = {}
    return render (request, "saco_arena.html", context)

def barnis(request):
    context = {}
    return render (request, "pages/barnis.html", context)

def ceramica(request):
    context = {}
    return render (request, "pages/ceramica.html", context)


""" HERRANIENTAS MANUALES """
def herramientas(request):
    context = {}
    return render (request, "pages/herramientas_manuales.html", context)

def atornillador(request):
    context = {}
    return render (request, "pages/ator_bosch.html", context)

def martillo(request):
    context = {}
    return render (request, "pages/martillo.html", context) 

def llave_francesa(request):
    context = {}
    return render (request, "pages/llave_francesa.html", context)

def lijadora(request):
    context = {}
    return render (request, "pages/lijadora.html", context)

def sierra_circular(request):
    context = {}
    return render (request, "pages/sierra_cir.html", context)

def ator_inalambrico(request):
    context = {}
    return render (request, "pages/ator_inalambrico", context)

def taladro (request):
    context = {}
    return render (request, "pages/taladro.html", context)


""" CRUD'S """

@login_required
def crud(request):
    usuario = Usuario.objects.all()
    context = {
        "usuarios": usuario,
    }
    return render(request, "pages/crud.html", context)

def user_add(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        cargos = Cargo.objects.all()
        context = {
            "generos": generos,
            "cargos": cargos,
        }
        return render(request, "pages/user_add.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        cargo = request.POST["cargo"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True

        objGenero = Genero.objects.get(id_genero=genero)
        objCargo = Cargo.objects.get(id_cargo=cargo)

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            id_cargo=objCargo,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/user_add.html", context)
    
def user_update(request):
    if request.method=="POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        genero = request.POST["genero"]
        cargo = request.POST["nombre_cargo"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        direccion = request.POST["direccion"]
        activo = True
        objGenero = Genero.objects.get(id_genero=genero)
        objCargo = Cargo.objects.get(id_cargo=cargo)
        obj = Usuario(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            id_cargo=objCargo,
            telefono=telefono,
            email=correo,
            password=password,
            direccion=direccion,
            activo=activo,
        )
        obj.save()

        generos = Genero.objects.all()
        cargos = Cargo.objects.all()
        context = {
            "mensaje": "Modificado con Exito",
            "generos":generos,
            "usuario":obj,
            "cargos":cargos,
        }
        return render(request, "pages/user_update.html", context)
    
def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username=="admin" and password=="1234":
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {

        }
        return render(request,"pages/login.html",context)    
    
def user_del(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)
        usuario.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro Eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error,Rut no encontrado...",
            "usuarios": usuarios,
        }
        return render(request, "pages/crud.html", context)
    
def user_findEdit(request,pk):
    if pk!="":
        """ 
            objects.get() = Obtener datos con filtro
            objects.all() = Obtener todos
        """
        usuario = Usuario.objects.get(rut=pk)
        generos = Genero.objects.all()

        context={
            "usuario":usuario,
            "generos":generos,
        }
        return render(request,"pages/user_update.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje":"Error,Rut no encontrado",
            "usuarios":usuarios
        }
        return render(request,"pages/crud.html",context)
    
def desconectar(request):   
    if request.user.is_authenticated:
        logout(request)
    
    context = {
        "mensaje":"Desconectado con exito",
        "design":"alert alert-success w-50 mx-auto text-center",
    }
    return render(request,"pages/login.html",context)

def conectar(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/crud.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"pages/login.html",context)
    else:
        context = {

        }
        return render(request,"pages/login.html",context)

def catalogo(request):
    productos = Producto.objects.all()
    context = {
        "productos":productos,
    }
    return render (request, "pages/catalogo.html", context) 

def producto_add(request):
    if request.method != "POST":
        categorias = Categoria.objects.all()
        context = {
            "categorias":categorias,
        }
        return render(request, "pages/producto_add.html", context)
    else:
        nombre_producto = request.POST["nombre_producto"]
        precio = request.POST["precio"]
        categoria = request.POST["categoria"]
        img_producto = request.POST["img_producto"]
        descripcion = request.POST["descripcion"]

        objCategoria = Categoria.objects.get(id_categoria=categoria)
        
        obj = Producto.objects.create(
            nom_producto = nombre_producto,
            preciopro = precio,
            id_categoria = objCategoria,
            img_pro = img_producto,
            descrip = descripcion,
        )
        obj.save()
        context = {
            "aviso": "Producto creado correctamente!!!"
        }
        return render (request, "pages/producto_add.html", context)
