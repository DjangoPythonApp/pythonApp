from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')

        if not name:
            self.add_error('name', "Name cannot be empty")

        if price is not None and price <= 0:
            self.add_error('price', "Price must be greater than 0")

        return cleaned_data