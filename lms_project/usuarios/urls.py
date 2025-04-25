from django.urls import path
from .views import (
    RegistroView,
    redirecionar_usuario,
    area_aluno,
    painel_professor,
)

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('redirecionar/', redirecionar_usuario, name='redirecionar_usuario'),
    path('aluno/', area_aluno, name='area_aluno'),
    path('painel/', painel_professor, name='painel_professor'),
]
