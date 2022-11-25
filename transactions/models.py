from django.db import models


class Type(models.Model):
    descricao = models.CharField(max_length=23)
    natureza = models.CharField(max_length=7)
    sinal = models.CharField(max_length=1)


class Transaction(models.Model):
    tipo = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="transacoes")
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    hora = models.TimeField()
    dono = models.CharField(max_length=14)
    nome = models.CharField(max_length=19)

    def get_time(self):
        return self.hora.strftime("%H:%M:%S")

    def get_value(self):
        return f"R${round(self.valor / 100, 2)}".replace(".", ",")

    def get_date(self):
        return self.data.strftime("%d/%m/%Y")
