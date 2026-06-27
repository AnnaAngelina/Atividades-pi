from django.db import models

# Create your models here.
class Livro(models.Model):
    titulo = models.CharField(max_length=100, default='Título', null=False)
    autor = models.CharField(max_length=200)
    ano = models.PositiveIntegerField()
    prioridade_leitura = models.PositiveIntegerField(help_text='Digite um número de 1 a 5')
    sinopse = models.TextField()

    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo