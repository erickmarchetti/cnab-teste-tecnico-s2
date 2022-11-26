from django.shortcuts import render
from .forms import TransactionForm

from .models import Transaction
from .serializers import TransactionSerializer
from utils.services import (
    get_values_from_file,
    group_by_store,
    decode_serializer_errors,
)


def transactionListCreate(request):

    if request.method == "GET":
        form = TransactionForm()

        transactions = Transaction.objects.all()
        transaction_groups = group_by_store(transactions)

        context = {
            "form": form,
            "transaction_groups": transaction_groups,
        }

        return render(request, "index.html", context)

    if request.method == "POST":
        form = TransactionForm()
        context = {"form": form}

        file = request.FILES["file"].file
        transaction_data_list, file_errors = get_values_from_file(file)

        if file_errors:
            context["file_errors"] = file_errors
            context["has_errors"] = True
            return render(request, "index.html", context)

        serializer = TransactionSerializer(data=transaction_data_list, many=True)

        if not serializer.is_valid():
            context["serializer_errors"] = decode_serializer_errors(serializer)
            context["has_errors"] = True
            return render(request, "index.html", context)

        serializer.save()

        transactions = Transaction.objects.all()
        transaction_groups = group_by_store(transactions)

        context["transaction_groups"] = transaction_groups

        return render(request, "index.html", context)
