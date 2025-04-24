from django.contrib.auth.models import AbstractUser
from django.db import models 

class User(AbstractUser):
    TIPO_USUARIO= [
        ('aluno','Aluno'),
        ('professor','Professor'),
    ]
    tipo= models.CharField(max_length=10,choices=TIPO_USUARIO, default='aluno')

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"