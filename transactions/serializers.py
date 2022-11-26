from rest_framework import serializers

from .models import Transaction, Type

from utils.services import formatting_time, formatting_date


class TransactionSerializer(serializers.ModelSerializer):
    tipo_id = serializers.ChoiceField(
        choices=[transaction.id for transaction in Type.objects.all()],
        error_messages={"invalid_choice": "Tipo inválido, verifique a tabela de tipos"},
    )
    data = serializers.IntegerField(
        error_messages={"invalid": "Data deve ser um inteiro"}
    )
    hora = serializers.IntegerField(
        error_messages={"invalid": "Hora deve ser um inteiro"}
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

    def create(self, validated_data: dict):
        validated_data["hora"] = formatting_time(f"00000{validated_data['hora']}"[-6:])
        # ainda tem erros aqui
        validated_data["data"] = formatting_date(f"{validated_data['data']}")

        # Transaction.objects.create(validated_data)
        # print(validated_data)
        ...
