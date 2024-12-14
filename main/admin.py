from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import *
admin.site.unregister(Group)
admin.site.unregister(User)
class ClubInline(admin.StackedInline):
    model = Club
    extra = 1
class PlayerInline(admin.StackedInline):
    model = Player
    extra = 1
class TransferInline(admin.StackedInline):
    model = Transfer
    extra = 1


@admin.register(Country)
class Country(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    inlines = (ClubInline,)

@admin.register(Club)
class Club(admin.ModelAdmin):
    list_display = ("name", "president",  "coach",  "found_date",   "max_import","max_export")
    search_fields = ('name','president','coach', )
    inlines = (PlayerInline,)

@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display = ('name', 'position', 'age', 'price', 'number','club', 'country', )
    search_fields = ('name','number', )
    filter_fields = ('club','country',)

@admin.register(Season)
class Season(admin.ModelAdmin):
    list_display = ('name',  )
    search_fields = ('name', )
    inlines = (TransferInline,)

@admin.register(Transfer)
class Transfer(admin.ModelAdmin):
    list_display = (  'club_old', 'club_new',  'player', 'price', 'price_tft','season',)
    search_fields = ('player','club_old', 'club_new', 'season' )
    filter_fields = ('club_old','club_new','season','player',)


