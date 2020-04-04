# creato io
from django.conf.urls import url
from . import views

#aggiunta da tutorial
app_name = 'groups'

urlpatterns = [

    url(r'^$', 
    views.ListGroups.as_view(), 
    name='all'),

    url(r'^new/$', 
    views.CreateGroups.as_view(), 
    name='create'),

    url(r'^posts/in/(?P<slug>[-\w]+)/$', """ slugifica il nome del gruppo  """ 
    views.SingleGroups.as_view(), 
    name='single'),