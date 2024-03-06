from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
