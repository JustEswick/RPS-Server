from rest_framework import routers
from games.api import MatchViewSet, RecordViewSet
from django.urls import include, path
from games.views import Play
router = routers.DefaultRouter()

router.register('matches', MatchViewSet, basename='matches')
router.register('records', RecordViewSet, basename='records')


urlpatterns = [
    path('play/', Play.as_view(), name='play'),
    path('', include(router.urls))
]
