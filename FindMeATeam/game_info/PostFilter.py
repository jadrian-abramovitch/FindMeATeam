import django_filters
from . import models

class PostFilter(django_filters.FilterSet):
	class Meta:
		model = models.GameInfo()
		fields = ['rank', 'positions_played', 'server']