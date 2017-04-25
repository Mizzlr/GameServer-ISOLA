from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Match(models.Model):
    codebot1 = models.ForeignKey('CodeBot', models.CASCADE,
        related_name='match_codebot1', db_column='codebot1')
    codebot2 = models.ForeignKey('CodeBot', models.CASCADE,
        related_name='match_codebot2', db_column='codebot2')
    winner = models.ForeignKey('Player', models.CASCADE,
        related_name='match_winner', db_column='winner', null=True)
    runner = models.ForeignKey('Player', models.CASCADE,
        related_name='match_runner', db_column='runner', null=True)

class Player(models.Model):
    name = models.CharField(max_length=30)

class History(models.Model):
    match = models.ForeignKey('Match', models.CASCADE, db_column='match')
    time = models.DateTimeField()
    move = models.TextField() # some json blob so that this is game agnostic

class CodeBot(models.Model):
    player = models.ForeignKey('Player', models.CASCADE, db_column='player')
    code = models.TextField() # source code of the bot, any language
    lang = models.CharField(max_length=10, choices=[('python', 'python')])