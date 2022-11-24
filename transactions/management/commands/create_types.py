from transactions.models import Type
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help: str = "Cria tipos prontos na model type"

    types = [
        {"descricao": "Débito", "sinal": "+"},
        {"descricao": "Boleto", "sinal": "-"},
        {"descricao": "Financiamento", "sinal": "-"},
        {"descricao": "Crédito", "sinal": "+"},
        {"descricao": "Recebimento Empréstimo", "sinal": "+"},
        {"descricao": "Vendas", "sinal": "+"},
        {"descricao": "Recebimento TED", "sinal": "+"},
        {"descricao": "Recebimento DOC", "sinal": "+"},
        {"descricao": "Aluguel", "sinal": "-"},
    ]

    def handle(self, *args, **options):
        for type in self.types:
            type["natureza"] = "Entrada" if type["sinal"] == "+" else "Saída"

            new_type = Type(**type)
            new_type.full_clean()

            new_type.save()
