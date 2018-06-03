from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from results.models import Match, Score


class MatchResource(ModelResource):
    scores = fields.ToManyField('results.api.resources.ScoreResource', 'score_set', full=True)

    class Meta:
        queryset = Match.objects.all()
        allowed_methods = ['get', 'post']
        authorization = Authorization()


class ScoreResource(ModelResource):
    class Meta:
        queryset = Score.objects.all()
        allowed_methods = ['get']
