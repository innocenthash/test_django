from django.contrib import admin

from Tache.models import Tache
@admin.register(Tache)
class AdminTache(admin.ModelAdmin):
    list_display = ["nom", "description","date_creation","fait"]
# Register your models here.
