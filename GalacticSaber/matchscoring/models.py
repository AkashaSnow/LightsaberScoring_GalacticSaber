from django.db import models

# Create your models here.

class Score(models.Model):
    score_text = models.CharField(max_length=200)

    def __str__(self):
        return self.score_text

class Timer(models.Model):
    timer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.timer_text