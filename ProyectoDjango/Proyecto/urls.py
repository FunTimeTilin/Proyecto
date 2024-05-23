from ProyectoDjango.urls import path
from Proyecto import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("EPP", views.EPP, name="EPP"),
]