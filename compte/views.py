from django.shortcuts import render
from django.contrib import messages

from compte.models import User
from django.contrib.auth import authenticate,login 
def user_registration_view(request,*args, **kwargs):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        passwordconfirm = request.POST.get('passwordconfirm')
        email = request.POST.get('email')
        if password != passwordconfirm:
            messages.error(request,'Les mots de passe ne correspondent pas')
            # pour verifier l'existence de user
        elif User.objects.filter(username=username).exists():
            messages.error(request, "ce nom d'utilisation existe déjà")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "cet email  existe déjà")
        else:
            user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            
                                            email=email)
            user.save()
            user.is_active = False

            messages.success(request, 'Votre compte a été crée avec succès')
    return render(request, 'registration/registration.html',{})

def user_login_view(request,*args, **kwargs):
      if request.method == "POST" :
          username=request.POST.get('username')
          password=request.POST.get('password')
          user= User.objects.filter(username=username)
          if user.exists():
              if user.first().is_active :
                  user=authenticate(username=username, password=password)
                  if user is not None:
                      login(request,user)

                      messages.success(request,'vous etes connecté')
                  else:
                      messages.error(request,"Le nom d'utilisateur ou le mot de passe est incorrect")
              else:
                  messages.error(request, "Votre compte n'est pas encore activé . Veuillez verifier votre boite email")
          else:
              messages.error(request,"Le nom d'utilisateur ou le mot de passe est incorrect")
      return render(request, 'registration/login.html', {})
      
                      # User is authenticated
          

# Create your views here.
