from django.contrib import admin

# Register your models here.
from results.models import Match, Score

admin.site.register(Match)
admin.site.register(Score)
