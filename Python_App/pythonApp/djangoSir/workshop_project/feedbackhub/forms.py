from django import forms

TOPIC_CHOICES = [
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Machine Learning', 'Machine Learning'),
    ('Data Science', 'Data Science')
]

RATING_CHOICES = [
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Average', 'Average'),
    ('Poor', 'Poor')
]

class FeedbackForm(forms.Form):
    participant_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    workshop_topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    rating = forms.ChoiceField(choices=RATING_CHOICES)
    comments = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(required=False)

    def clean_comments(self):
        comments = self.cleaned_data['comments']
        if len(comments) < 5:
            raise forms.ValidationError(
                "Comments must contain at least 20 characters."
            )
        return comments

    def clean_attachment(self):
        file = self.cleaned_data.get('attachment')
        if file:
            allowed_extensions = [
                '.pdf',
                '.docx',
                '.txt'
            ]
            filename = file.name.lower()

            if not any(filename.endswith(ext)for ext in allowed_extensions):
                raise forms.ValidationError(
                    "Only PDF, DOCX and TXT files are allowed."
                )
        return file