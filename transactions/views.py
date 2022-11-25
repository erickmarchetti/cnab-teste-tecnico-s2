from django.shortcuts import render
from .forms import TransactionForm

from .models import Transaction
from utils.services import get_values_from_file, group_by_store


def transactionListCreate(request):

    if request.method == "GET":
        transactions = Transaction.objects.all()
        transaction_groups = group_by_store(transactions)

        form = TransactionForm()

        context = {
            "form": form,
            "transaction_groups": transaction_groups,
        }

        return render(request, "index.html", context)

    if request.method == "POST":

        file = request.FILES["file"].file

        transaction_data_list, file_errors = get_values_from_file(file)

        if not file_errors:
            for transaction_data in transaction_data_list:
                Transaction.objects.create(**transaction_data)

        transactions = Transaction.objects.all()
        transaction_groups = group_by_store(transactions)

        form = TransactionForm()

        context = {
            "form": form,
            "transaction_groups": transaction_groups,
            "file_errors": file_errors,
        }

        return render(request, "index.html", context)
