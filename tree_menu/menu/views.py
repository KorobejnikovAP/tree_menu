from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexMenuPage(TemplateView):
    template_name = 'menu/index.html'
