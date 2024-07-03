

from django.urls import path
from Tache.views import TacheDeleteView, TacheDetailView, TacheListView

app_name = "tache"
urlpatterns = [
    path("tache_list/", TacheListView.as_view(), name="tache_list"),
    path("tache_detail/<int:pk>/", TacheDetailView.as_view(), name="tache_detail"),
    path("tache_delete/<int:pk>/", TacheDeleteView.as_view(), name="tache_delete"),
]
