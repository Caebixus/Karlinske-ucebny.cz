from django.urls import path, include

from . import views

urlpatterns = [
    path('ucebna_A', views.ucebna_A, name='ucebna_A'),
    path('ucebna_B', views.ucebna_B, name='ucebna_B'),
    path('ucebna_C', views.ucebna_C, name='ucebna_C'),
]
