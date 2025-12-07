from rest_framework import serializers
from games.models import Match, Record


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = (
            "id", "player", "player_choice", "machine_choice", "result", "created_at",
        )
        read_only_fields = (
            "id", "player", "player_choice", "machine_choice", "result", "created_at",
        )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ["player_choice"]


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            "id", "player", "created_at", "updated_at", "record", "is_current_record"
        )
        read_only_fields = (
            "id", "player", "created_at", "updated_at", "record", "is_current_record"
        )
