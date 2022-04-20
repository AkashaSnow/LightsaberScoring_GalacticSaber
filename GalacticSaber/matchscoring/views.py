from re import template
from django.shortcuts import render
from django.views import generic

# Create your views here.

from django.http import HttpResponse

from .models import Score, Timer


class ScoreView(generic.ListView):
    model = Score
    template_name = 'matchscoring/score.html'

    


