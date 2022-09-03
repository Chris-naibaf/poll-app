from django.urls import path  # Del paquete django, módulo urls, importa la funcion path

from . import views  # Desde este mismo directorio importa el módulo views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
