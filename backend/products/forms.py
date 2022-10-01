
from django import forms
from products.models import Product


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        field = [
            'title',
            'content',
            'price'
        ]
