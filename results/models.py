from django.db import models


class Match(models.Model):
    timestamp = models.DateTimeField()
    gamemode = models.CharField(max_length=10)
    dmflags = models.PositiveIntegerField()
    dmflags2 = models.PositiveIntegerField()
    zadmflags = models.PositiveIntegerField()
    compatflags = models.PositiveIntegerField()
    compatdmflags2 = models.PositiveIntegerField()
    zacompatflags = models.PositiveIntegerField()


class Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.PROTECT)
    wins = models.IntegerField()
    frags = models.IntegerField()
    deaths = models.IntegerField()
    handicap = models.IntegerField()
    time = models.IntegerField()
    isbot = models.BooleanField()
    account = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
