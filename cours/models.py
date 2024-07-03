
from django.db import models
from django.urls import reverse

# Create your models here.

class Cour(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    

    class Meta:
        verbose_name = ("Cour")
        verbose_name_plural = ("Cours")

    def __str__(self):
        return self.nom

    def get_absolute_url(self):
        return reverse("detail_cours", kwargs={"pk": self.pk})
class ImageCours(models.Model):
    cours = models.ForeignKey(Cour,on_delete=models.CASCADE)
    images = models.ImageField(upload_to= "media")
