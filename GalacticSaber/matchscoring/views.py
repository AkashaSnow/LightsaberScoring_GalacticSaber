from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

from .models import Score


class ScoreView(generic.ListView):
    model = Score
    template_name = 'matchscoring/score.html'