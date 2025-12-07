from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Player(AbstractUser):

    @property
    def total_wins(self):
        return self.matches.filter(result='W').count()

    @property
    def total_losses(self):
        return self.matches.filter(result='L').count()

    @property
    def total_draws(self):
        return self.matches.filter(result='D').count()

    @property
    def total_games(self):
        return self.matches.count()

    @property
    def win_rate(self):
        total = self.total_games
        if total == 0:
            return 0
        return self.total_wins / total
