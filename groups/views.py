from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic

from groups.models import Group, GroupMember

from django.shortcuts import get_object_or_404
from django.contrib import messages

from django.db import IntegrityError


# Create your views here.

# class based views, perche ereditano da altre classi

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    # questo va connesso al group creato nel modello
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

# quel LoginRequiredMixin fa si che non devo mettere il login required probabilmente
class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        
        # setto l'errore specifico
        except IntegrityError:
            messages.warning(self.request, "Sei già membro di questo gruppo!")
        else:
            messages.success(self.request, "Ti sei iscritto al gruppo!")

        return super().get(request, *args, **kwargs)

            

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single", kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            # eliminato models. prima di groupmember
            membership = GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'Mi spiace ma non sei nel gruppo')

        else:
            membership.delete()
            messages.success(self.request, 'Ti sei cancellato dal gruppo')
            
        return super().get(request, *args, **kwargs)
