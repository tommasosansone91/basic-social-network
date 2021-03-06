from django.db import models
from django.urls import reverse #ho corretto io, ersione di django cambiata
from django.conf import settings

import misaka as m

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()
# connette il post a chi si logga come user

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)

    # quando qualcuno fa un post, il tempo di creazione è automaticamente aggiunto
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    # editable=False perchè non vuoi che le personesiano in grado  di editare

    group = models.ForeignKey(Group, related_name="posts", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = m.html(self.message)
        # in questo modo quando si fa un markdon si mette un link nel loro post
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username':self.user, 'pk':self.pk})

    class Meta:
            ordering = ['-created_at']
            unique_together = ['user', 'message'] # per far si che sia legato in modo univoco ad un user
            
