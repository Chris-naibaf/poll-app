from django.urls import path  # Del paquete django, módulo urls, importa la funcion path

from . import views  # Desde este mismo directorio importa el módulo views

urlpatterns = [
    path("", views.index, name="index"),
]
