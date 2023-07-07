from django.urls import path, include
from .views import home, registro, macetas, plantas, tierras, jaja, agregar, agregar2, agregar3, listar, modificar, modificar2, eliminar, eliminar2, modificar3, eliminar3

urlpatterns = [
    path('', home, name="home"),
    path('macetas/', macetas, name="macetas"),
    path('plantas/', plantas, name="plantas"),
    path('tierras/', tierras, name="tierras"),
    path('jaja/', jaja, name="jaja"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro, name="registro"),
    path('agregar/', agregar, name="agregar"),
    path('agregar2/', agregar2, name="agregar2"),
    path('agregar3/', agregar3, name="agregar3"),
    path('listar/', listar, name="listar"),
    path('modificar/<id>/', modificar, name="modificar"),
    path('modificar2/<id>/', modificar2, name="modificar2"),
    path('modificar3/<id>/', modificar3, name="modificar3"),
    path('eliminar/<id>/', eliminar, name="eliminar"),
    path('eliminar2/<id>/', eliminar2, name="eliminar2"),
    path('eliminar3/<id>/', eliminar3, name="eliminar3"),

]
