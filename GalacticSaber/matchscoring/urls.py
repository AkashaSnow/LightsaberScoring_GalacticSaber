from django.urls import path

from . import views

app_name = 'matchscoring'
urlpatterns = [
    path('score', views.ScoreView.as_view(), name='score'),
    path('timer', views.timer), 

    ]


