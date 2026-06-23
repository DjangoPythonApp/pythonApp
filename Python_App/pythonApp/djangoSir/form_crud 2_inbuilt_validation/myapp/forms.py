from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    def clean_name(self):
        name = self.cleaned_data.get('name')
        name = name.strip()
        print(f'Length of name: {len(name)}')
        
        if len(name) < 3:
            raise forms.ValidationError("Product name must be at least 3 characters long.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']


# forms.Form we donot have Table involve

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.FloatField()
#     description = forms.CharField(widget=forms.Textarea)