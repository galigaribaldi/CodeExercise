from django.db import models
from model_utils.models import TimeStampedModel, SoftDeletableModel

class Pokemon(TimeStampedModel, SoftDeletableModel):
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=50, blank=True)
    growth_time         = models.IntegerField(blank=True)
    natural             = models.CharField(blank=True, max_length=50)
    preEvolution        = models.CharField(blank=True, max_length=100, help_text="Escriba la evolución anterior, si no la conoce; déjelo en blanco")
    evolution           = models.CharField(blank=True, max_length=100, help_text="Escriba la evolución siguiente, si no la conoce; déjelo en blanco")
    max_harvest         = models.IntegerField(blank=True)
    natural_gift_power  = models.IntegerField(blank=True)
    size                = models.IntegerField(blank=True)
    smoothness          = models.IntegerField(blank=True)
    soil_dryness        = models.IntegerField(blank=True)
    date_published 		= models.DateTimeField(auto_now_add=True, verbose_name="date published")
    potency             = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name

class PokemonTrainer(TimeStampedModel, SoftDeletableModel):
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=50, blank=True)
    age                 = models.FloatField(blank=True)
    origin_city         = models.CharField(max_length=100, blank=True)
    gender              = models.CharField(max_length=3)
    region_name         = models.CharField(max_length=100)
    is_training         = models.BooleanField()
    pokemon             = models.ManyToManyField(Pokemon, help_text="Seleccione un Pokemon para éste entrenador")
    def __str__(self):
        return self.name

class PokemonTeam(TimeStampedModel, SoftDeletableModel):
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length=50, blank=True)
    origin_city         = models.CharField(max_length=100, blank=True)
    region_name         = models.CharField(max_length=100)
    number_wins         = models.IntegerField(blank=True)
    pokemonTrainer      = models.ManyToManyField(PokemonTrainer, help_text="Seleccione un Entrenador para formar un Team")
    def __str__(self):
        return self.name

class PokemonTeamOnly(TimeStampedModel, SoftDeletableModel):
    id                  = models.AutoField(primary_key=True)
    nameTeam            = models.CharField(max_length=50, blank=True)
    onlyPokemon         = models.BooleanField()
    pokemon             = models.ManyToManyField(Pokemon, help_text="Seleccione un Pokemon para éste entrenador")
    def __str__(self):
        return self.nameTeam