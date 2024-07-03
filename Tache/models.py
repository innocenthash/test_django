from django.db import models
from django.urls import reverse

class Tache(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    date_creation = models.DateField()
    fait = models.BooleanField()
# Create your models here.


    def get_absolute_url_for_detail(self):
     return reverse("tache:tache_detail", kwargs={"pk": self.pk})
    
    def get_absolute_url_for_delete(self):
     return reverse("tache:tache_delete", kwargs={"pk": self.pk})
    
    
