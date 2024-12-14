from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class BaseModels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
         abstract = True

class  Country(BaseModels):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Countries"

class  Club(BaseModels):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clubs')
    president = models.CharField(max_length=255)
    coach = models.CharField(max_length=255,blank=True,null=True)
    found_date = models.DateTimeField(blank=True,null=True)
    max_import = models.FloatField(blank=True,null=True)
    max_export = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.name

class Player(BaseModels):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=255,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True,validators=[MinValueValidator(16),MaxValueValidator(40)])
    price = models.FloatField(blank=True,null=True)
    number = models.IntegerField(blank=True,null=True)
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} ({self.club.name})"


class Season(BaseModels):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class  Transfer(BaseModels):
    club_old = models.ForeignKey(Club, on_delete=models.CASCADE,related_name='club_old' )
    club_new = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='club_new')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    price = models.FloatField(blank=True, null=True)
    price_tft  =models.FloatField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.player.name}: {self.club_old.name} -> {self.club_new.name}"