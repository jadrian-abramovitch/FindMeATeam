from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import datetime



class GameInfo(models.Model):
	LEAGUE_OF_LEGENDS = "LOL"
	games = [
		(LEAGUE_OF_LEGENDS, 'League of Legends')
	]

	game_icons = {
		LEAGUE_OF_LEGENDS: "/../staticfiles/LOL-logo.jpg"
	}
	

	positions = [
		('Top', 'Top'),
		('Jungle', 'Jungle'),
		('Mid', 'Mid'),
		('Bot', 'Bot'), 
		('Support', 'Support')
	]

	ranks = [
		('Challenger', 'Challenger'),
		('GrandMaster', 'GrandMaster'),
		('Master', 'Master'),
		('Diamond', 'Diamond'),
		('Platinum', 'Platinum'),
		('Gold', 'Gold'),
		('Silver', 'Silver'),
		('Bronze', 'Bronze'),
		('Iron', 'Iron')
	]

	servers = [
		('BR', 'BR'),
		('EUNE', 'EUNE'),
		('EUW', 'EUW'),
		('LAN', 'LAN'),
		('LAS', 'LAS'),
		('NA', 'NA'),
		('OCE', 'OCE'),
		('RU', 'RU'),
		('TR', 'TR'),
		('JP', 'JP'),
		('KR', 'KR'),
		('CN', 'CN'),
		('TW', 'TW'),
		('SAM', 'SAM'),
		('VN', 'VN'),
		('TH', 'TH'),
		('PH', 'PH')
	]

	times = []
	for i in range(24):
		times += [(str(i), str(i)+":00" + " (EST)")]


	game = models.CharField(max_length=20, choices=games, default=LEAGUE_OF_LEGENDS)
	positions_played = models.CharField(max_length=7, choices=positions, default='Top')
	rank = models.CharField(max_length=20, choices=ranks, default='Challenger')
	server = models.CharField(max_length=5, choices=servers, default='NA')
	start_Time_Available = models.CharField(max_length=20, choices=times, default='0')
	end_Time_Available = models.CharField(max_length=20, choices=times, default='0')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	in_game_name = models.CharField(max_length = 30)

	def __str__(self):
		return self.game

	def get_absolute_url(self):
		return reverse('home')

	# def get_icon_location(self):
	# 	return game_icons[self.game]

	game_icon = game_icons[game]
