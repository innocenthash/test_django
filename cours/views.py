# from msilib.schema import ListView
from django.shortcuts import get_object_or_404, redirect, render

from django.urls import reverse
from django.views import View
from django.views.generic import (ListView,DetailView , CreateView , UpdateView,DeleteView)
from cours.forms import CourForm
from cours.models import Cour

# Create your views here.

class CourViewMixin(object):
    model : Cour
    def get_object(self):
        pk= self.kwargs.get('pk')
        obj = None
        if pk is not None : 
            obj = get_object_or_404(Cour,pk=pk)
        return obj  
    
class CourListView(ListView):
    model = Cour
    template_name = "cours/cours_list.html"
    queryset = Cour.objects.all()


class CourDetailView(DetailView):
    model = Cour
    template_name = "cours/cours_details.html"
    queryset = Cour.objects.all()

class CourCreateView(CreateView):
    model = Cour
    form_class=CourForm
    template_name = "cours/cours_create.html"
    queryset = Cour.objects.all()
    def form_valid(self, form):
        nom = form.cleaned_data.get('nom')
        if nom == 'Français':
            form.add_error("nom", "ce cours n'est pas autorisé")
            return self.form_invalid(form)
        return super().form_valid(form)
    

class CourUpdateView(UpdateView):
    model = Cour
    form_class=CourForm
    template_name = "cours/cours_update.html"
    queryset = Cour.objects.all()


class CourDeleteView(DeleteView):
    model = Cour
    template_name = "cours/cours_delete.html"
    queryset = Cour.objects.all()
    def get_success_url(self) :
        return reverse('cours_list')

class FcoursListView(View):
    template_name = "cours/cours_list.html"
    def get(self, request, *args, **kwargs):
        queryset = Cour.objects.all()
        context = {
            'object_list':queryset
        }
        return render(request, self.template_name,context)

class FcourDetailView(View):
    template_name = "cours/cours_details.html"
   
    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None :
            obj = get_object_or_404(Cour,pk=pk)
            context = {
                "object":obj
            }
        return render(request, self.template_name,context)
class FCourCreateView(View):
    form = CourForm()
    template_name = "cours/cours_create.html"
    context = {
        'form':form
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = CourForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('cours_list')
        return render(request, self.template_name,self.context)

class FCourUpdateView(View):
    template_name = "cours/cours_update.html"
    def get_object(self):
        pk= self.kwargs.get('pk')
        obj = None
        if pk is not None : 
            obj = get_object_or_404(Cour,pk=pk)
        return obj
    def get(self, request, *args, **kwargs):
        context = {
            'form':CourForm(instance=self.get_object())
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = CourForm(request.POST , instance=self.get_object()) 
        if form.is_valid():
            form.save()
            return redirect('cours_list')
        return render(request, self.template_name,{'form':form})

class FCourDeleteView(View,CourViewMixin):
    template_name = "cours/cours_delete.html"
    # def get_object(self):
    #     pk= self.kwargs.get('pk')
    #     obj = None
    #     if pk is not None : 
    #         obj = get_object_or_404(Cour,pk=pk)
    #     return obj
    def get(self, request, *args, **kwargs):
        context = {
            'object':self.get_object()
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('cours_list')
        return render(request, self.template_name,{'object':obj})

