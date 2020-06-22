from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse





class GameInfo(models.Model):
	game = models.CharField(max_length=100)
	positions_played = models.CharField(max_length=100)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.game

	def get_absolute_url(self):
		return reverse('home')



