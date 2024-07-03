from ProyectoDjango.urls import path
from Proyecto import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("EPP", views.EPP, name="EPP"),
    path("login", views.conectar, name="login"),
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
    path("crud", views.crud, name="crud"),
    path("user_add", views.user_add, name="user_add"),
    path("user_update", views.user_update, name="user_update"),
    path("user_del/<str:pk>", views.user_del, name="user_del"),
    path("user_findEdit/<str:pk>", views.user_findEdit, name="user_findEdit"),
    path("crud_genero", views.crud_genero, name="crud_genero"),
    path("genero_add", views.genero_add, name="genero_add"),
    path("genero_del/<str:pk>", views.genero_del, name="genero_del"),
    path("genero_edit/<str:pk>", views.genero_edit, name="genero_edit"),
    path("logout", views.desconectar, name="logout"),
]