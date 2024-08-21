from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),  # Página de inicio
    path('Contacto/', contacto, name='Contacto'),
    path('Nosotros/', nosotros, name='Nosotros'),
]
