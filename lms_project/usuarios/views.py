from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CustomUserCreationForm
from .models import User

class RegistroView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')

@login_required
def redirecionar_usuario(request):
    if request.user.tipo == 'aluno':
        return redirect('/cursos/')
    elif request.user.tipo == 'professor':
        return redirect('/painel/')
    else:
        return redirect('/admin/')
