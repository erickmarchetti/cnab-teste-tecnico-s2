from django.forms import ModelForm, FileField
from .models import Shop


class ShopForm(ModelForm):
    file = FileField()

    class Meta:
        model = Shop
        fields = ["file"]


file = ShopForm.base_fields["file"]
file.widget.attrs["accept"] = ".txt"
