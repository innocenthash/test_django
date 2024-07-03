
from django import forms

from produits.models import Produits


class ProduitsForm(forms.ModelForm):
    
    class Meta:
        model = Produits
        fields = ("nom","description","prix",'active')
    
    def clean_nom(self,*args, **kwargs):
        nom = self.cleaned_data.get('nom')
        if nom == "zaza" :
            raise forms.ValidationError("Le nom du produit ne doit pas etre vide")
        return nom
class PureProduitsForm(forms.Form):
    nom =  forms.CharField(required=False , widget=forms.TextInput(attrs={'class':'name', "placeholder":'Entrez le nom du produit'}))
    description = forms.CharField(required=False , widget=forms.Textarea(attrs = {
         'rows':30 ,
         "cols":10 ,
         'class' : 'description',
         'id' : 'description'
    }))
    prix = forms.FloatField(required=False, label='prix du produit', initial='12.00')
    active = forms.BooleanField(required=False , help_text='pour nous aider si ça vous plait ou pas ')
