from datetime import time, date

# Model Shop
def formatting_data(date_str: str):
    return date(
        year=int(date_str[:4]),
        month=int(date_str[4:6]),
        day=int(date_str[6:]),
    )


def formatting_time(time_str: str):
    return time(
        hour=int(time_str[:2]),
        minute=int(time_str[2:4]),
        second=int(time_str[4:]),
    )


def get_values_from_file(file):
    expected_fields = [
        {"name": "tipo_id", "start": 0, "end": 1},
        {"name": "data", "start": 1, "end": 9, "formatting": formatting_data},
        {"name": "valor", "start": 9, "end": 19},
        {"name": "cpf", "start": 19, "end": 30},
        {"name": "cartao", "start": 30, "end": 42},
        {"name": "hora", "start": 42, "end": 48, "formatting": formatting_time},
        {"name": "dono", "start": 48, "end": 62},
        {"name": "nome", "start": 62, "end": 81},
    ]

    lines = file.readlines()

    shop_data_list = []

    for line in lines:
        shop_data = {}

        for field in expected_fields:
            byte: bytes = line[field["start"] : field["end"]]
            formated_string = byte.decode("utf8").lstrip().rstrip()

            if field.get("formatting", None):
                function = field["formatting"]
                formated_string = function(formated_string)

            shop_data[field["name"]] = formated_string

        shop_data_list.append(shop_data)

    return shop_data_list
