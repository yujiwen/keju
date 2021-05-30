from keju.views import KejuContextMixin
from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class KejuTemplateView(KejuContextMixin, TemplateView):
    template_name = "pstc/index.html"

def import_public_salary_table():
    pass