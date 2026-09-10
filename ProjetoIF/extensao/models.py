from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

class PerfilAcademico(models.Model):
    link_lattes = models.URLField()
    biografia = models.TextField()
    aluno = models.OneToOneField(Aluno, on_delete=models.SET_NULL, related_name='perfilAcademico', null=True, blank=True)

    def __str__(self):
        return f'{self.link_lattes} - {self.aluno.nome}'

class Projeto(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    data_inicio = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='projeto', null=True, blank=True)
    equipe = models.ManyToManyField(Aluno, related_name='projeto')

    def __str__(self):
        return self.titulo
