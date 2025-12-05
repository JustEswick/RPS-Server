from django.contrib.auth import logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.


class WhoAmI(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        return Response({"username": request.user.username})


class LogoutView(APIView):

    def get(self, request):
        logout(request)  # elimina la sesión
        return Response({"detail": "Logged out successfully"})
