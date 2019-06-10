from django.urls import path, include

from . import views

urlpatterns = [
    path('ucebna-A', views.ucebna_A, name='ucebna_A'),
    path('ucebna-B', views.ucebna_B, name='ucebna_B'),
    path('ucebna-C', views.ucebna_C, name='ucebna_C'),
]
