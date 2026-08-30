from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=100, null=True)
    email = models.EmailField(blank=True)
    ano_nascimento = models.DateField(null=True)

    def __str__(self):
        return self.nome