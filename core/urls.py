# URLS/CORE

from . import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    #path('', views.mostrarHTML, name='mostrarHTML'),
    path('', views.registro_view, name='registro'),
]
