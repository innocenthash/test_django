from django.db import models
from django.urls import reverse

# Create your models here.

class Produits(models.Model):
    nom  = models.name = models.CharField(max_length=50)
    description = models.TextField(blank=True , null=True)
    prix = models.DecimalField(max_digits=10000 , decimal_places = 2 )
    active = models.BooleanField(null=True)
    is_deleted = models.BooleanField(null=True)
    
    def get_absolute_url_for_detail(self):
        return reverse("page:produit_details_view", kwargs={"id": self.pk})
    def get_absolute_url_for_delete(self):
        return reverse("page:produit_delete_view", kwargs={"id": self.pk})
    
    def __str__(self):
        return self.nom




