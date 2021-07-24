from django.db import models

# Create your models h
class CountryGame(models.Model):
    country_id=models.AutoField
    country_name=models.CharField(max_length=30,default="")
    country_represnt=models.CharField(max_length=20,default="")
    country_noTeams=models.IntegerField(default=0)
    country_flag=models.ImageField(upload_to='country/images',default="")

    def __str__(self):
        return self.country_name

class Games(models.Model):
    game_id=models.IntegerField(default=0)
    game_name=models.CharField(max_length=40,default="")
    game_noParti=models.IntegerField(default=0)

    def __str__(self):
        return self.game_name