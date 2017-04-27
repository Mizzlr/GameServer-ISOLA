from django.shortcuts import render
from rest_framework import viewsets

from gameservice import models
from gameservice import serializers

# Create your views here.
class ContestViewSet(viewsets.ModelViewSet):
    queryset = models.Contest.objects.all()
    serializer_class = serializers.ContestSerializer

class NestedContestHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ContestHistory.objects.all()
    serializer_class = serializers.ContestHistorySerializer

    def list(self, request, contest_pk=None):
        queryset = models.ContestHistory.objects.filter(contest_pk=contest_pk).order_by('creation_time')
        serializer = serializers.ContestHistorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, contest_pk=None):
        queryset = models.ContestHistory.objects.filter(pk=pk, contest_pk=contest_pk)
        history = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ContestHistorySerializer(history)
        return Response(serializer.data)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = models.Submission.objects.all()
    serializer_class = serializers.SubmissionSerializer