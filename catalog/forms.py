from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductForm(ModelForm):

    class Meta(ModelForm):
        model = Product
        fields = (
            "name",
            "description",
            "photo",
            "is_published",
            "price",
        )


    def clean_name(self):
        name = self.cleaned_data['name']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if name in forbidden_words:
            raise ValidationError("Нельзя создавать продукты с запрещенными словами в названии")
        return name


class VersionForm(ModelForm):

    class Meta(ModelForm):
        model = Version
        fields = "__all__"