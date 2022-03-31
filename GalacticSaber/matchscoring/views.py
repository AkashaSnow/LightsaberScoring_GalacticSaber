from re import template
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Score


class ScoreView(generic.ListView):
    model = Score
    template_name = 'matchscoring/score.html'

class IndexView(generic.DetailView):
    template_name = 'matchscoring/timer.py'
    template_name = 'matchscoring/timer.html'

