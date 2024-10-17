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


class ProductForm(StyleMixin, ModelForm):

    class Meta:
        model = Product
        fields = (
            "name",
            "category",
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


    def clean_description(self):
        description = self.cleaned_data['description']
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if description in forbidden_words:
            raise ValidationError("Нельзя создавать продукты с запрещенными словами в описании продукта")
        return description


class VersionForm(StyleMixin, ModelForm):

    class Meta:
        model = Version
        fields = "__all__"
