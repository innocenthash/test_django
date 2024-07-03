from django import forms
from Tache.models import Tache


class TacheForm(forms.ModelForm):
    
    class Meta:
        model = Tache
        fields = ("nom","description","date_creation","fait")
