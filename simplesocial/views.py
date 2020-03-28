# questo file l'ho creato manualmente sotto simple social, 
# devo tenerci le views che vanno bene per tutto il progetto

from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = "thanks.html"