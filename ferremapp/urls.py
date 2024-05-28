from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('vendedor/', vendedor, name='vendedor'),
    path('bodeguero/', bodeguero, name='bodeguero'),
    path('contador/', contador, name='contador'),
    path('cliente/', cliente, name='cliente'),
    path('epp/', epp, name='epp'),
    path('acercade/', acercade, name='acercade'),
    path('contacto/', contacto, name='contacto'),
    path('carrito/', carrito, name='carrito'),
    path('catalogo/', catalogo, name='catalogo'),
    path('herramientasmanuales/', herramientasmanuales, name='herramientasmanuales'),
    path('materialesligeros/', materialesligeros, name='materialesligeros'),
    path('pint_ext/', pint_ext, name='pint_ext'),
    path('piso_flot/', piso_flotante, name='piso_flotante'),
    path('buscar/', buscarSeries, name='buscarSeries'),
    path('api/', include(router.urls)),
    path('api/productos/', obtener_producto, name='obtener_producto'),
    path('productos/', listar_productos, name='listar_productos'),
    path('epp/antiparra/', antiparra, name='antiparra'),
    path('epp/guantes/', guantes, name='guantes'),
    path('epp/protectoroido/', protectoroido, name='protectoroido'),
    path('epp/mascara/', mascara, name='mascara'),
    path('epp/zapatoseguridad/', zapatoseguridad, name='zapatoseguridad'),
    path('initiate_payment/', initiate_payment, name='initiate_payment'),
    path('payment_confirm/', payment_confirm, name='payment_confirm'),
]