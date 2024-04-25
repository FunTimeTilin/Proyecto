from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('vendedor/', views.vendedor, name='vendedor'),
    path('bodeguero/', views.bodeguero, name='bodeguero'),
    path('contador/', views.contador, name='contador'),
    path('cliente/', views.cliente, name='cliente'),
    path('epp/', views.epp, name='epp'),
    path('acercade/', views.acercade, name='acercade'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('herramientasmanuales/', views.herramientasmanuales, name='herramientasmanuales'),
    path('materialesligeros/', views.materialesligeros, name='materialesligeros'),
    path('pint_ext/', views.pint_ext, name='pint_ext'),
    path('piso_flot/', views.piso_flotante, name='piso_flotante'),
    
]