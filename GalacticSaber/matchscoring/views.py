from re import template
from django.shortcuts import render
from django.views import generic
<<<<<<< HEAD


# Create your views here.

=======
>>>>>>> 185150c1afebd2bbae6b68ecef260c0ce2accb06
from django.http import HttpResponse

from .models import Score

<<<<<<< HEAD
class IndexView(generic.DetailView):
    template_name = 'matchscoring/matchScoring.html'

class IndexView(generic.DetailView):
    template_name = 'matchscoring/timer.py'
    template_name = 'matchscoring/timer.html'
=======

class ScoreView(generic.ListView):
    model = Score
    template_name = 'matchscoring/score.html'
>>>>>>> 185150c1afebd2bbae6b68ecef260c0ce2accb06
