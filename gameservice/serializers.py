from rest_framework import serializers
from gameservice import models

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Match
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.History
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'

class CodeBotSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CodeBot
        fields = '__all__'
