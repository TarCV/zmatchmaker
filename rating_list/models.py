from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=30)
    verified = models.BooleanField()

    def __str__(self):
        return "{} ({})".format(self.name, "verified" if self.verified else "assumed")


class Discipline(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rating(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)
    rating = models.FloatField()
    variance = models.FloatField()

    def __str__(self):
        return "{} - {} - {} {}".format(self.player.name, self.discipline.name, self.rating, self.variance)
