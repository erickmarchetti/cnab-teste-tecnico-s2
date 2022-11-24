from django.shortcuts import render
from .forms import ShopForm

from .models import Shop
from utils.services import get_values_from_file


def shopListCreate(request):
    context = ...

    if request.method == "GET":
        form = ShopForm()

        context = {
            "form": form,
        }

    if request.method == "POST":

        file = request.FILES["file"].file

        shop_data_list = get_values_from_file(file)
        shop_instance_list = [
            Shop.objects.create(**shop_data) for shop_data in shop_data_list
        ]

        form = ShopForm()

        context = {
            "form": form,
        }

    return render(request, "index.html", context)
