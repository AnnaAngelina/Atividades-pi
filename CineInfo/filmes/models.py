from django.db import models

# Create your models here.
class Filme(models.Model):
    titulo = models.CharField(max_length=200, default='titulo', null=False)
    ano = models.PositiveIntegerField()
    nota = models.PositiveIntegerField(default=0, help_text='digite uma nota de 0 a 5')
    sinopse = models.TextField()

    class Meta:
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return f'{self.titulo} ({self.ano})'