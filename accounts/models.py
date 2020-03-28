
# del tutorial, sono errate dopo aggiornamento django
# from django.db import models
# from django.contrib import auth

from django.contrib.auth import models

# Create your models here.

# modello per accounts
class User(models.User, models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)