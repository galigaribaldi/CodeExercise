from dataclasses import fields
from rest_framework import serializers
from Pokeapi.models import Pokemon, PokemonTrainer, PokemonTeam, PokemonTeamOnly

class PokeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'growth_time', 'max_harvest', 'natural', 'preEvolution', 'evolution','natural','natural_gift_power', 'size', 'smoothness', 'soil_dryness', 'potency']

class PokeTrainerSerializers(serializers.ModelSerializer):
    class Meta:
        model = PokemonTrainer
        fields = ['id','name','age','origin_city', 'gender', 'region_name', 'is_training', 'pokemon']

class PokeTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonTeam
        fields = ['id','name','origin_city', 'region_name', 'number_wins', 'pokemonTrainer']

class PokeTeamOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonTeamOnly
        fields = ['id','nameTeam', 'onlyPokemon', 'pokemon']