from django import forms
from .models import Media

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ["type", "title", "director", "cast", "country", "date_added", "release_year",
                  "rating", "duration", "listed_in", "description"]