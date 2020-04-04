from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic

from groups.models import Group, GroupMember
# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # questo va connesso al group creato nel modello
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group