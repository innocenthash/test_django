from django import forms
from cours.models import Cour


class CourForm(forms.ModelForm):
    
    class Meta:
        model = Cour
        fields = ("nom", "description")
