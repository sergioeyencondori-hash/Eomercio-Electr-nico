from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('acercade/', views.acercade, name='acercade'),
    path('contacto/', views.contacto, name='contacto'),
]
