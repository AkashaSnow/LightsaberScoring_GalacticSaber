from re import template
from django.shortcuts import render
from django.views import generic


# Create your views here.

from django.http import HttpResponse


class IndexView(generic.DetailView):
    template_name = 'matchscoring/matchScoring.html'

class IndexView(generic.DetailView):
    template_name = 'matchscoring/timer.py'
    template_name = 'matchscoring/timer.html'