from django.contrib.auth import get_user_model
from users.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, status, filters
from users.models import Player
from users.serializers import PlayerSerializer

from rest_framework import viewsets, permissions


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlayerSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


User = get_user_model()


class Register(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
