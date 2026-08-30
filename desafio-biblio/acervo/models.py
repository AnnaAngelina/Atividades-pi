from django.db import models
from autor import models as m

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    data_publicacao = models.PositiveSmallIntegerField(blank=True)
    resumo = models.TextField(blank=True)
    nome_editora = models.CharField(max_length=100, blank=True)
    autor = models.ForeignKey(m.Autor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo