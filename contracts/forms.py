from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'product', 'document', 'conclusion_date', 'validity_period', 'amount']
        widgets = {
            'conclusion_date': forms.DateInput(attrs={'type': 'date'}),
        }
