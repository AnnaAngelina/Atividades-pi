from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=200, null=False, default='aluno')
    matricula = models.CharField(max_length=20, null=False)

    class Meta:
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f"{self.nome} - {self.matricula}"