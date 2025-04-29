

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
from .decorators import somente_alunos, somente_professores


class RegistroView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')

@login_required
def redirecionar_usuario(request):
    if request.user.tipo == 'aluno':
        return redirect('/usuarios/aluno/')
    elif request.user.tipo == 'professor':
        return redirect('/usuarios/painel/')
    else:
        return redirect('/admin/')

from django.shortcuts import render

@login_required
@somente_alunos
def area_aluno(request):
    return render(request, 'usuarios/area_aluno.html')

@login_required
@somente_professores
def painel_professor(request):
    return render(request, 'usuarios/painel_professor.html')
