from django.urls import path, include

from . import views

urlpatterns = [
    path('rezervace', views.rezervace, name='rezervace'),
    path('rezervace_poslana', views.rezervace_poslana, name='rezervace_poslana'),
]
