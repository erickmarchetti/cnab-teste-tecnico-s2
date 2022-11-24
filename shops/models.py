from django.db import models


class Type(models.Model):
    descricao = models.CharField(max_length=23)
    natureza = models.CharField(max_length=7)
    sinal = models.CharField(max_length=1)


class Shop(models.Model):
    tipo = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="loja")
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono = models.CharField(max_length=14)
    nome = models.CharField(max_length=19)
