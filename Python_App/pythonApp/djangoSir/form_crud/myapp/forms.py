from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = name.strip() if name else ''
        if not name:
            raise forms.ValidationError('Name cannot be empty')
        # do not accept any numbers in the name
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Name cannot contain numbers')
        if len(name) < 3:
            raise forms.ValidationError('Name must be at least 3 characters long')
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None:
            raise forms.ValidationError('Price is required')
        if price <= 0:
            raise forms.ValidationError('Price must be greater than 0')
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        description = description.strip() if description else ''
        if not description:
            raise forms.ValidationError('Description cannot be empty')
        if len(description) < 10:
            raise forms.ValidationError('Description must be at least 10 characters long')
        return description