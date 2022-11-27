from rest_framework import serializers

from .models import Transaction, Type


class TransactionSerializer(serializers.ModelSerializer):
    tipo_id = serializers.IntegerField(
        error_messages={"invalid": "Tipo inválido, verifique a tabela de tipos"},
    )
    data = serializers.DateField(
        input_formats=["%Y%m%d"],
        error_messages={"invalid": "Data deve ser válida"},
    )
    hora = serializers.TimeField(
        input_formats=["%H%M%S"],
        error_messages={"invalid": "Hora deve ser válida"},
    )
    valor = serializers.IntegerField(
        error_messages={"invalid": "Valor deve ser um inteiro"}
    )

    class Meta:
        model = Transaction
        fields = [
            "tipo_id",
            "data",
            "valor",
            "cpf",
            "cartao",
            "hora",
            "dono",
            "nome",
        ]
