from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'cost']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
