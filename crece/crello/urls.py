from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contenedorTablero/', views.consultar_tab, name='consultar_tab'),
    path('crearTablero/', views.crear_tab, name='crear_tab'),
    path('editarTablero/<int:id>', views.editar_tab, name='editar_tab'),
    path('eliminarTablero/<int:id>', views.eliminar_tab, name='eliminar_tab'),
    path('tablero/<int:id>', views.consultar_lista, name='consultar_lista'),
    path('crearLista/<int:id>', views.crear_lista, name='crear_lista'),
    path('editarLista/<int:id>', views.editar_lista, name='editar_lista'),
    path('eliminarLista/<int:id>', views.eliminar_lista, name='eliminar_lista'),
    path('crearTarjeta/<int:id>', views.crear_tarjeta, name='crear_tarjeta'),
    path('editarTarjeta/<int:id>', views.editar_tarjeta, name='editar_tarjeta'),
    path('eliminarTarjeta/<int:id>', views.eliminar_tarjeta, name='eliminar_tarjeta'),
]
