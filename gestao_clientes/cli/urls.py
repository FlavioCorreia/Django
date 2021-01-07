from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete

urlpatterns = [
    path('list/', persons_list, name='persons_list'), #LISTAR USUARIOS CADASTRADOS
    path('new/', persons_new, name='person_new'), #FORMULARIO P/ CADASTRAR NOVO USUARIO
    path('update/<int:id>/', persons_update, name='persons_update'), #FUNCAO DE UPDATE DE USUARIO
    path('delete/<int:id>/', persons_delete, name='persons_delete'), #FUNCAO DE DELETE DE USUARIO
]
