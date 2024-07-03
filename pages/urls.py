"""
URL configuration for test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import *

app_name = "page"
urlpatterns = [
  
    path('',home_view,name='home'),
    path('contact',contact_view,name='contact'),
    path('about',about_view,name='about'),
    path('details',detail_view,name='details'),
    path('all',all_view,name='all'),
    path('create_produit',produit_create_view,name='create_produit'),
    path("produit/detail/<int:id>/", produit_details_view, name="produit_details_view"),
    path("produit/delete/<int:id>/", produit_delete_view, name="produit_delete_view"),
]
