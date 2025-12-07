from django.db import models
from users.models import Player
from random import choice
from typing import Optional
# Create your models here.


class Record(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="records", verbose_name="Player"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, blank=False, verbose_name="Creation date")

    updated_at = models.DateTimeField(
        auto_now=True, blank=False, verbose_name="Update date")

    record = models.PositiveSmallIntegerField(
        default=0, editable=True, verbose_name="Record")

    is_current_record = models.BooleanField(
        default=True, editable=True, verbose_name="Is actual record")

    @classmethod
    def get_last_record(cls, player: Player):
        try:
            record = Record.objects.get(player=player, is_current_record=True)
        except Record.DoesNotExist:
            record = Record.objects.create(
                player=player, record=0, is_current_record=True)
        except Record.MultipleObjectsReturned:
            records = Record.objects.filter(
                player=player, is_current_record=True)
            record = records.first()
            records.exclude(id=record.id).update(is_current_record=False)

        return record

    @classmethod
    def update_record(cls, player: Player, won: bool):
        record = Record.get_last_record(player=player)
        if won:
            record.record += 1
        elif record.record > 0:
            record.is_current_record = False

        class Meta:
            verbose_name = "Streak Record"
            ordering = ["-updated_at", ]

        record.save()

        return record

    def __str__(self):
        return f"{self.player.username}'s {"active" if self.is_current_record else "inactive"} Record is {self.record} in {self.updated_at}"


class Match(models.Model):

    CHOICES = [
        ("R", "Rock"),
        ("P", "Paper"),
        ("S", "Scissors"),
        ("L", "Lizard"),
        ("Sp", "Spock"),
    ]

    RESULTS = [
        ("W", "Win"),
        ("L", "Loss"),
        ("D", "Draw"),
    ]

    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="matches", verbose_name="Player")

    player_choice = models.CharField(
        max_length=2, choices=CHOICES, blank=False, verbose_name="Player choice")
    machine_choice = models.CharField(
        max_length=2, choices=CHOICES, blank=False, verbose_name="Machine choice")

    # The results of the match for the player
    result = models.CharField(
        max_length=1, choices=RESULTS, blank=False, verbose_name="Result")

    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, blank=False, verbose_name="Created at")

    def save(self, *args, **kwargs):

        if not self.machine_choice:
            self.machine_choice = choice(self.CHOICES)[0]

        self.result = self.get_result()

        super().save(*args, **kwargs)

    def get_result(self):

        if self.player_choice == self.machine_choice:
            return "D"  # Draw

        # Rock vs Scissors:
        if self.player_choice == "R" and self.machine_choice == "S":
            return "W"

        # Rock vs Lizard:
        if self.player_choice == "R" and self.machine_choice == "L":
            return "W"

        # Scissors vs Paper:
        if self.player_choice == "S" and self.machine_choice == "P":
            return "W"

        # Scissors vs Lizard:
        if self.player_choice == "S" and self.machine_choice == "L":
            return "W"

        # Paper vs Rock:
        if self.player_choice == "P" and self.machine_choice == "R":
            return "W"

        # Paper vs Spock:
        if self.player_choice == "P" and self.machine_choice == "Sp":
            return "W"

        # Lizard vs Paper:
        if self.player_choice == "L" and self.machine_choice == "P":
            return "W"

        # Lizard vs Spock:
        if self.player_choice == "L" and self.machine_choice == "Sp":
            return "W"

        # Spock vs Scissor:
        if self.player_choice == "Sp" and self.machine_choice == "S":
            return "W"

        # Spock vs Rock:
        if self.player_choice == "Sp" and self.machine_choice == "R":
            return "W"

        return "L"

    def __str__(self):
        return f"{self.player.username} {self.result} against vs Machine at {self.created_at}"
