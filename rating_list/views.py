from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Discipline, Rating, Player


def index(request):
    disciplines = Discipline.objects.order_by('name')
    context = {
        'disciplines': disciplines
    }
    return render(request, 'index.html', context)


def discipline(request, id):
    ratings = Rating.objects \
        .filter(discipline=id) \
        .order_by('-rating')
    context = {
        'ratings': ratings
    }
    return render(request, 'discipline.html', context)


def player(request, id):
    player = get_object_or_404(Player, pk=id)
    ratings = player.rating_set.order_by('discipline__name')
    return render(request, 'player.html', {'player': player, 'ratings': ratings})
