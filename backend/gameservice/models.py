from __future__ import unicode_literals
from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    creation_time = models.DateTimeField()
    starter = models.TextField() # source code that emits the starting board configuration
    umpire = models.TextField() # source code of umpire that will check that validity of the game
    language = models.CharField(max_length=10, choices=[('python', 'python')], default='python')
    creation_time = models.DateTimeField()
    max_moves = models.IntegerField(default=100)

class Player(models.Model):
    name = models.CharField(max_length=30)
    creation_time = models.DateTimeField()

class Contest(models.Model):
    player1 = models.ForeignKey('Player', models.CASCADE, related_name='contest_player1', db_column='player1')
    player2 = models.ForeignKey('Player', models.CASCADE, related_name='contest_player2', db_column='player2')
    options = models.TextField() # input passed to the Game.starter too generate the starting board
    starter = models.CharField(max_length=10, choices=[('Player1', 'Player1'), ('Player2', 'Player2')], default='Player1')
    submission1 = models.ForeignKey('Submission', models.CASCADE, related_name='contest_submission1', db_column='submission1')
    submission2 = models.ForeignKey('Submission', models.CASCADE, related_name='contest_submission2', db_column='submission2')
    winner = models.CharField(max_length=10, choices=[('Player1', 'Player1'), ('Player2', 'Player2')], null=True)
    creation_time = models.DateTimeField()

class ContestHistory(models.Model):
    contest = models.ForeignKey('Contest', models.CASCADE, db_column='contest')
    player = models.ForeignKey('Player', models.CASCADE, db_column='player')
    move_played = models.TextField() # some json blob so that this is game agnostic
    creation_time = models.DateTimeField()

class Submission(models.Model):
    player = models.ForeignKey('Player', models.CASCADE, db_column='player')
    code_snippet = models.TextField() # source code of the bot, any language
    language = models.CharField(max_length=10, choices=[('python', 'python')], default='python')
    creation_time = models.DateTimeField()
