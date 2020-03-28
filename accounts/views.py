from django.shortcuts import render

# ricorda se uno è logged in o 0out dove deve andare
# from django.core.urlresolvers import reverse_lazy

# cambiato io, prima era django.core.urlresolvers, update django
from django.urls import reverse_lazy

from django.views.generic import TemplateView
from . import forms

# dava nome non definito per createview, l'ho aggiunto io
from django.views.generic.edit import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    # praticamente reverse lazy non reindirizza finchè gli utenti non hanno premuto su submit
    template_name = 'accounts/signup.html'
    
