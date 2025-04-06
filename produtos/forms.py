from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
        }