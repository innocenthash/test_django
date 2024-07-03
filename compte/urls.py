
from django.urls import path
from compte import views

app_name="compte"
urlpatterns = [
      path("register/", views.user_registration_view, name="register"),
      path("connecter/", views.user_login_view, name="connecter")
]
