from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from results.models import Match, Score


def score_hidden_fields():
    return ['id', 'resource_uri', 'match']


class ScoreResource(ModelResource):
    match = fields.ToOneField('results.api.resources.MatchResource', 'match')

    def dehydrate(self, bundle):
        for field in score_hidden_fields():
            if field in bundle.data:
                del bundle.data[field]
        return super().dehydrate(bundle)

    class Meta:
        resource_name = 'score'
        queryset = Score.objects.all()
        excludes = score_hidden_fields()
        authorization = Authorization()


class MatchResource(ModelResource):
    scores = fields.ToManyField(ScoreResource, 'score_set', related_name='match', full=True)

    class Meta:
        resource_name = 'match'
        queryset = Match.objects.all()
        allowed_methods = ['get', 'post']
        excludes = ['id', 'resource_uri']
        authorization = Authorization()
