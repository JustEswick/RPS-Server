from games.models import Match, Record
from games.serializers import MatchSerializer, RecordSerializer
from rest_framework import generics, status, filters


from rest_framework import viewsets, permissions


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MatchSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['player__username']


class RecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Record.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RecordSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['player__username']
