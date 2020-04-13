# creato io
from django.conf.urls import url
from . import views

#aggiunta da tutorial
app_name = 'posts'

urlpatterns = [

    url(r'^$', 
    views.PostList.as_view(), 
    name='all'),

    url(r'new/$', 
    views.CreatePost.as_view(), 
    name='create'),

    # <username> è un argomento che gli viene passato in ingresso
    url(r'by/(?P<username>[-\w]+)', 
    views.UserPosts.as_view(), 
    name='for_user'),

    # questo mostra tutti i post dello user
    url(r'by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', 
    views.PostDetail.as_view(), 
    name='single'),
     

    url(r'delete/(?P<pk>/d+)/$', 
    views.DeletePost.as_view(), 
    name='delete'),

]