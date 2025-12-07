from django.contrib import admin
from games.models import Match, Record

# Register your models here.


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
