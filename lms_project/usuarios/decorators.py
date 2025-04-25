from django.core.exceptions import PermissionDenied

def somente_alunos(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.tipo != 'aluno':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def somente_professores(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.tipo != 'professor':
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view
