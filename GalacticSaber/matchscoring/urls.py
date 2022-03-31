from django.urls import path

from . import views

app_name = 'matchscoring'
urlpatterns = [path('', views.ScoreView.as_view(), name='score'),]

