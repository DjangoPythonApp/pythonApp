from django import forms


class PlacementPredictionForm(forms.Form):
    cgpa = forms.FloatField(
        label="CGPA",
        min_value=0,
        max_value=10,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter CGPA",
                "step": "0.01",
            }
        ),
    )

    aptitude = forms.FloatField(
        label="Aptitude Score",
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter aptitude score",
                "step": "0.01",
            }
        ),
    )