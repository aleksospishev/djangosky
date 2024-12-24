from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator

from .models import Product

WORDS_LIST_EXCLUDE = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()

    class Meta:
        model = Product
        exclude = ["created_at", "updated_at", "owner"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Наименование продукта"})
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Описание продукта", "rows": 5}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Цена продукта", "type": "number", "min": 0, "step": 10}
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        for word in name.lower().split():
            if word in WORDS_LIST_EXCLUDE:
                self.add_error("name", f"Наименование не может содержать слово {word}")

        for word in description.lower().split():
            if word in WORDS_LIST_EXCLUDE:
                self.add_error("description", f"Описание не может содержать слово {word}")


class ProductModeratorForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "published",
        ]
