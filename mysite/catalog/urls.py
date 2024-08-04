from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_ejemplos, name='lista_ejemplos'),
    path('crear/', views.crear_ejemplo, name='crear_ejemplo'),
    path('editar/<int:id>/', views.editar_ejemplo, name='editar_ejemplo'),
    path('eliminar/<int:id>/', views.eliminar_ejemplo, name='eliminar_ejemplo'),
]