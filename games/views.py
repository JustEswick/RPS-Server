from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from games.models import Match, Record
from games.serializers import GameSerializer
# Create your views here.


class Play(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication, JWTAuthentication]
    serializer_class = GameSerializer

    def post(self, request, *args, **kwargs):

        player_choice = request.data.get("player_choice")

        if player_choice not in [c[0] for c in Match.CHOICES]:
            return Response({"error": "Invalid option"}, status=status.HTTP_400_BAD_REQUEST)

        player_match = Match.objects.create(
            player=request.user,
            player_choice=player_choice
        )

        if not player_match.result == "D":
            Record.update_record(
                player=request.user,
                won=player_match.result == "W"
            )

        return Response({
            "id": player_match.id,
            "player": player_match.player.id,
            "player_choice": player_match.player_choice,
            "machine_choice": player_match.machine_choice,
            "result": player_match.result,
            "created_at": player_match.created_at,
        }, status=status.HTTP_201_CREATED)
