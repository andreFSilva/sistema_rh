from django.db import models


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do funcionario')
    sobreno = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + ' ' + self.sobreno
