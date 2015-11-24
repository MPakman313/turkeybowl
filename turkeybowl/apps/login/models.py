from django.db import models
from datetime import datetime, time
mytime = datetime.now()
formatted_time = mytime.strftime("%Y-%m-%d")


class Player(models.Model):
	name = models.CharField(max_length=255)
	class Meta:
		db_table = 'players'


class Team(models.Model):
	team_name = models.CharField(max_length=255)
	players = models.ForeignKey(Player)
	email = models.CharField(max_length=255)
	pref_time = models.DateField()
	pref_location = models.CharField(max_length=255)
	class Meta:
		db_table = 'teams'
	