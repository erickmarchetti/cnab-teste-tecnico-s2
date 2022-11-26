from datetime import time, date
from transactions.models import Transaction


class Store:
    def __init__(self, name=None) -> None:
        self.name = name
        self.transactions: list[Transaction] = []
        self.balance = 0

    def get_balance(self):
        return f"R${round(self.balance / 100, 2)}".replace(".", ",")


def formatting_date(date_str: str):
    return date(
        year=int(date_str[:4]),
        month=int(date_str[4:6]),
        day=int(date_str[6:]),
    )


def formatting_time(time_str: str):
    print(time_str)
    return time(
        hour=int(time_str[:2]),
        minute=int(time_str[2:4]),
        second=int(time_str[4:]),
    )


def check_lines(file_lines: list[bytes]):
    decoded_lines = [line.decode("utf-8").rstrip("\n") for line in file_lines]

    errors = []
    for position, line in enumerate(decoded_lines, 1):
        if len(line) != 80:
            errors.append(f"A linha {position} deve ter exatamente 80 caracteres")

    return errors


def get_transaction_data(lines, transaction_data_list):
    expected_fields = [
        {"name": "tipo_id", "start": 0, "end": 1},
        {"name": "data", "start": 1, "end": 9},
        {"name": "valor", "start": 9, "end": 19},
        {"name": "cpf", "start": 19, "end": 30},
        {"name": "cartao", "start": 30, "end": 42},
        {"name": "hora", "start": 42, "end": 48},
        {"name": "dono", "start": 48, "end": 62},
        {"name": "nome", "start": 62, "end": 80},
    ]

    for line in lines:
        transaction_data = {}
        line = line.decode("utf-8")

        for field in expected_fields:
            byte: bytes = line[field["start"] : field["end"]]

            formated_string = byte.lstrip().rstrip()

            transaction_data[field["name"]] = formated_string

        transaction_data_list.append(transaction_data)


def get_values_from_file(file):
    lines = file.readlines()

    transaction_data_list = []

    file_errors = check_lines(lines)
    if file_errors:
        return (transaction_data_list, file_errors)

    get_transaction_data(lines, transaction_data_list)

    return (transaction_data_list, file_errors)


def create_stores(queryset, transaction_groups: list[Store]):
    for transaction in queryset:
        store_name_list = [store.name for store in transaction_groups]

        if not transaction.nome in store_name_list:
            new_store = Store(transaction.nome)
            transaction_groups.append(new_store)


def group_by_store(queryset):
    transaction_groups: list[Store] = []

    create_stores(queryset, transaction_groups)

    for store in transaction_groups:
        for transaction in queryset:
            if store.name == transaction.nome:
                store.balance += (
                    transaction.valor
                    if transaction.tipo.sinal == "+"
                    else -transaction.valor
                )

                store.transactions.append(transaction)

    return transaction_groups
