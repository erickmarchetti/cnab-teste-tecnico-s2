from transactions.models import Transaction
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help: str = "Deleta todas as instancias da model Transaction"

    def handle(self, *args, **options):
        for transaction in Transaction.objects.all():
            transaction.delete()
