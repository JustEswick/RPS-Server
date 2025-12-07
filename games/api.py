from games.models import Match, Record
from games.serializers import MatchSerializer, RecordSerializer

from rest_framework import viewsets, permissions


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MatchSerializer


class RecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Record.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RecordSerializer
