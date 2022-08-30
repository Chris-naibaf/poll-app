# from django.shortcuts import render - Esto estaba aquí cuando llegué así
# que no lo eliminaré por el momento.
from django.http import HttpResponse

# Create your views here.

# Esta es una de las formas más sencillas de crear una vista.
def index(request):
    return HttpResponse("Hello, World. You're at the polls index.")
