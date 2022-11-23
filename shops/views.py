from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.shortcuts import render
from .forms import ShopForm

from .models import Shop
from .serializers import ShopSerializer


def shopListCreate(request):
    context = ...

    if request.method == "GET":
        form = ShopForm()

        context = {
            "form": form,
        }

    if request.method == "POST":
        form = ShopForm()

        context = {
            "form": form,
        }

    return render(request, "index.html", context)
