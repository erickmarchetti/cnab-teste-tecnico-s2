from django.forms import ModelForm, FileField
from .models import Shop


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"


teste = ShopForm.base_fields["teste"]
teste.widget.attrs["accept"] = ".txt"
