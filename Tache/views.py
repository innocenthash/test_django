
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView , DetailView , UpdateView ,DeleteView , CreateView
from Tache.models import Tache

class TacheListView(ListView):
    model = Tache
    context_object_name = 'taches'
    template_name='taches/tache_list.html'
    # paginate_by = 10
    def get_queryset(self):
        return Tache.objects.all().order_by('date_creation')


class TacheDetailView(DetailView):
    model = Tache
    template_name='taches/tache_detail.html'
    context_object_name = 'tache'
  
    # queryset=Tache.objects.all()
# Create your views here.


class TacheDeleteView(DeleteView):
    model = Tache
    context_object_name = 'tache'
    template_name = "taches/tache_delete.html"
    def get_success_url(self):
        return reverse("tache:tache_list")

class TacheUpdateView(UpdateView):
    model = Tache
    template_name = "taches/tache_detail.html"
    fields = ["nom","description","date_creation","fait"]

    def get_success_url(self):
        return reverse("taches/tache_detail.html",kwargs = {'pk':self.object.pk})
    

class TacheCreateView(CreateView):
    model = Tache
    template_name = "TEMPLATE_NAME"

