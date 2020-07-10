from django import forms

from products.models import Product

# Criação do formulário que será usado para inclusões e edições de produtos.
class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']