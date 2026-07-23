from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = name.strip()  # Remove leading and trailing whitespace
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) > 200:
            raise forms.ValidationError("Description cannot exceed 200 characters.")
        return description

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        labels = {
            'name': 'Name',
            'price': 'Price',
            'description': 'Description',
        }
