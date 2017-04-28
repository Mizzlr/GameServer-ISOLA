from rest_framework import serializers
from gameservice import models

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contest
        fields = '__all__'
        read_only = ('winner', 'creation_time')

class ContestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContestHistory
        fields = '__all__'
        read_only = ('creation_time')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'
        read_only = ('creation_time')

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Submission
        fields = '__all__'
        read_only = ('creation_time')
