from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render , get_object_or_404

from pages.forms import ProduitsForm, PureProduitsForm
from produits.models import Produits

# Create your views here.
# def home_view(request , *args, **kwargs):

#     return HttpResponse(request.user)
def home_view(request ,*args, **kwargs):
      list = [1,2,23,25]

      user = request.user 

      context = {
           'liste': list ,
            'user' : user
      }
      if user.is_authenticated :
           context['user'] = user.username
      else :
         context['user'] =  'utilisateur non authentifié' 
    
    
      return render(request,'home.html' , context)

def contact_view(request,*args, **kwargs):
    return render(request, 'contact.html' , {})

def about_view(request, *args, **kwargs):
     return render(request, 'about.html', {})

def detail_view(request , *args, **kwargs):
     obj = Produits.objects.get(id=1)
     context= {
          'nom':obj.nom,
          'description':obj.description ,
          'prix': obj.prix

     }

     return render(request,'contenue/detail.html' , context)

def all_view(request, *args, **kwargs) :
     obj= Produits.objects.all()
     context = {
          'produits':obj
     }
     
     return render(request, 'contenue/all.html', context)

# formulaire produit
def produit_create_view(request):
     form = ProduitsForm(request.POST or None)
     message = ""
     if request.method == "POST" :
       if form.is_valid():
           form.save()
           message = 'Le produit a été bien enregistrer'
           form = ProduitsForm()

                
     context={
            'form':form ,
             'message':message
          } 
     return render(request, "contenue/create_produit.html", context)

def produit_details_view(request,id):

     try:
           obj = Produits.objects.get(id=id)
           context = {
        "produit":obj
    }
     except Produits.DoesNotExist:
          raise Http404
     
          # comment: 
     # end try
    
#     obj= get_object_or_404(Produits,id=id)

    

     return render(request, "contenue/produit_details.html", context)

def produit_delete_view(request,id):
    obj = get_object_or_404(Produits , id=id)

    if request.method == "POST":
         obj.delete()
         return redirect('../../..')
    return render(request, "contenue/produit_delete.html", {"produit":obj})
    
#  formulaire produit mise a jour
# def produit_create_view(request):
#      obj = Produits.objects.get(id=1)
#      form = ProduitsForm(request.POST or None , instance=obj)
     
#      message = ""
#      if form.is_valid():
#           form.save()
#           message = 'Le produit a été bien enregistrer'
#           form = ProduitsForm()

#      context = {
#           'form':form ,
#           'message':message
#      }      
     
#      return render(request, "contenue/create_produit.html", context)
# formulaire avec html
# def produit_create_view(request):
#      message =  ""
#      if request.method == "POST" :
#           data =  request.POST
#           nom = data.get('nom')
#           description = data.get('description')
#           prix = data.get('prix')
#           # active = data.get('active')
#           active = 0
     
#           Produits.objects.create(nom=nom , description=description , prix=prix , active = active )

#           message = 'Produit créer avec succès !'
#      return render(request, "contenue/create_produit.html", {'message':message})
     
# def produit_create_view(request,*args, **kwargs):
#      message = ""
#      form = PureProduitsForm(request.POST or None)

#      if request.method == 'POST':
#         form = PureProduitsForm(request.POST)
#         if form.is_valid():
#             # Récupérer les données du formulaire
#             nom = form.cleaned_data['nom']
#             description = form.cleaned_data['description']
#             prix = form.cleaned_data['prix']
#             active = form.cleaned_data['active']

#             Produits.objects.create(
#                 nom=nom,
#                 description=description,
#                 prix=prix,
#                 active=active
#             )
#             # Vous pouvez maintenant utiliser ces données pour créer un nouvel objet Produit ou effectuer d'autres actions nécessaires
#             # Par exemple, si vous avez un modèle Produit, vous pouvez créer une instance ainsi :
#             # produit = Produit.objects.create(nom=nom, description=description, prix=prix, active=active)

#             # Ajoutez votre logique d'enregistrement ici
#             message = "Données enregistrées avec succès"
#             form = PureProduitsForm()
#              # Redirigez vers la vue appropriée après l'enregistrement
      
#      return render(request,"contenue/create_produit.html" , {"message":message , "form":form})
     
# end def   
    
    
# end def
     
    
# end def
    
