from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class indexview(TemplateView):
    template_name='users/index.html'
