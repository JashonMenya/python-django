from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields =('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title']
        # Convert title to lowercase
        title_lower = title.lower()
        if 'django' not in title_lower:
            raise ValidationError("We only accept notes about Django!")
        return title
