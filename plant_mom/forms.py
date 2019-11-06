from django import forms
from .models import Plant


class PlantForm(forms.ModelForm):

    class Meta:
        model = Plant
        fields = ('name', 'photo_url', 'description', 'care_tips', 'link',)
