from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),  
    path('contacto/', contacto, name='contacto'),
    path('Nosotros/', nosotros, name='Nosotros'),
]
