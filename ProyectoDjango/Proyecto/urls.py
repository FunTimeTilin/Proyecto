from ProyectoDjango.urls import path
from Proyecto import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("EPP", views.EPP, name="EPP"),
    path("inicio_sesion", views.inicio_sesion, name="inicio_sesion"),
    path("registro", views.registro, name="registro"),
    path("acercade", views.acercade, name="acercade"),
    path("antiparra", views.antiparra, name="antiparra"),
    path("carrito", views.carrito, name="carrito"),
    path("contacto", views.contacto, name="contacto"),
    path("guantes", views.guantes, name="guantes"),
    path("herramientas", views.herramientas, name="herramientas"),
    path("mascara", views.mascara, name="mascara"),
    path("materiales", views.materiales, name="materiales"),
    path("pintura", views.pintura, name="pintura"),
    path("piso", views.piso, name="piso"),
    path("protector", views.protector, name="protector"),
    path("zapatos", views.zapatos, name="zapatos"),
]