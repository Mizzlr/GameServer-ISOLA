from django.shortcuts import render
from rest_framework import viewsets

from gameservice import models
from gameservice import serializers

# Create your views here.
class MatchViewSet(viewsets.ModelViewSet):
    queryset = models.Match.objects.all()
    serializer_class = serializers.MatchSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = models.History.objects.all()
    serializer_class = serializers.HistorySerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

class CodeBotViewSet(viewsets.ModelViewSet):
    queryset = models.CodeBot.objects.all()
    serializer_class = serializers.CodeBotSerializer