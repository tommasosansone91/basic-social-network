#creato io

from django.conf.urls import url
from django.contrib.auth import views as auth_views
# uso alias: importala come views di autorizzazione così non faccio messup con altra variabile views
from . import views

#aggiunta da tutorial
app_name = 'accounts'

urlpatterns = [

    # pesca la funzione di vista dal modulo auth_views
    url(r'login/$', 
    auth_views.LoginView.as_view(template_name='accounts/login.html'), 
    name='login'),

    # pesca la funzione di vista dal modulo auth_views
    url(r'logout/$', 
    auth_views.LogoutView.as_view(), 
    name='logout'),

    # pesca la funzione di vista normalmente, da views.py
    url(r'signup/$', 
    views.SignUp.as_view(),
    name='signup')




]