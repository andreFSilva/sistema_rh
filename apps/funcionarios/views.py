from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


'''class FuncionariosView(TemplateView):
    template_name = 'base.html'''


def home(request):
    return HttpResponse('Ola mundo')
