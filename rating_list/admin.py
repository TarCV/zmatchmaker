from django.contrib import admin
from .models import Player, Discipline, Rating
# Register your models here.
admin.site.register(Player)
admin.site.register(Discipline)
admin.site.register(Rating)
