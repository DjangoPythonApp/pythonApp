from django import forms
from .models import Product
from .validation import regex_validator


class ProductForm(forms.ModelForm):

    @regex_validator(
        r'^[A-Za-z ]+$',
        'Product name can contain only letters and spaces.'
    )
    def clean_name(self):
        return self.cleaned_data.get('name').strip()

    @regex_validator(
        r'^[0-9]+(\.[0-9]{1,2})?$',
        'Price must be a valid positive number.'
    )
    def clean_price(self):

        price = self.cleaned_data.get('price')
        if price <= 0:
         raise forms.ValidationError(
            "Price must be greater than zero."
        )
        return str(price).strip()

    @regex_validator(
        r'^[A-Za-z0-9 ,.?!-]{10,}$',
        'Description must be at least 10 characters and contain only valid characters.'
    )
    def clean_description(self):
        return self.cleaned_data.get('description').strip()

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']


# forms.Form we donot have Table involve

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.FloatField()
#     description = forms.CharField(widget=forms.Textarea)