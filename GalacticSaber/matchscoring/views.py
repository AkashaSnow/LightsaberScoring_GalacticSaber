from re import template
from django.shortcuts import render
from django.views import generic
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 5794ab7cee12a6f51e481ba48c8409b350a1ee1d


# Create your views here.

<<<<<<< HEAD
=======
=======
>>>>>>> 185150c1afebd2bbae6b68ecef260c0ce2accb06
>>>>>>> 5794ab7cee12a6f51e481ba48c8409b350a1ee1d
from django.http import HttpResponse

from .models import Score


class ScoreView(generic.ListView):
    model = Score
    template_name = 'matchscoring/score.html'

class IndexView(generic.DetailView):
    template_name = 'matchscoring/timer.py'
    template_name = 'matchscoring/timer.html'

