from django.contrib import admin

# Register your models here.
from .models import Produits
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom' , "description","prix","active","is_deleted"]
    search_fields = ['nom',"description","active"]
    list_editable = ['prix',"active","is_deleted"]
    list_filter = ["prix","active", "is_deleted"]

admin.site.register(Produits,ProduitAdmin)

# admin.site.site_header = "" ,
# admin.site.site_title = "" ,
# admin.site.site_url = ""
# admin.site.index_title =  ""

