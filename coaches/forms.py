from django import forms
from coaches.models import Coaches

class CoachesForm(forms.ModelForm):
    class Meta:
        model = Coaches
        fields = ['name', 'background', 'imagepop']
