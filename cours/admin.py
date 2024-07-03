from django.contrib import admin

from cours.models import Cour, ImageCours


# @admin.register(Cour)
class ImagesCoursInline(admin.TabularInline):
    model = ImageCours
class AdminCour(admin.ModelAdmin):
    inlines = [
        ImagesCoursInline
    ]
    list_display = ['nom',"description"]
@admin.register(ImageCours)
class AdminImages(admin.ModelAdmin):
    list_display = ['cours','images']


# Register your models here.
admin.site.register(Cour,AdminCour)