from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PokeTrainerSerializers, PokeSerializers, PokeTeamSerializer, PokeTeamOnlySerializer
from .models import PokemonTrainer, Pokemon, PokemonTeam, PokemonTeamOnly
from rest_framework import status
from django.http import Http404
import logging

class Pokemon_APIView(APIView):
    """Class Pokemon to recive different web Methods (GET - POST - DELETE - PUT)
    If you don't have a id - Primarykey in Get method, you activate *Get ALL*
    """
    def get(self, request, pk=None):
        if pk is None:
            pokemon = Pokemon.objects.all()
            serializer = PokeSerializers(pokemon, many=True)
            return Response(serializer.data)
        else:
            try:
                pokemon = Pokemon.objects.get(pk=pk)
                serializer = PokeSerializers(pokemon)
                return Response(serializer.data)
            except:
                raise Http404
    def post(self, request, format = None):
        serializer = PokeSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pokemon = Pokemon.objects.get(pk=pk)
            pokemon.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        pokemon = Pokemon.objects.get(pk=pk)
        serializer = PokeSerializers(pokemon, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PokemonTrainer_APIView(APIView):
    """Class Pokemon Trainer to recive different web Methods (GET - POST - DELETE - PUT)
    If you don't have a id - Primarykey in Get method, you activate *Get ALL*
    """
    def get(self, request, pk=None):
        if pk is None:
            pokemonTrainer = PokemonTrainer.objects.all()
            serializer = PokeTrainerSerializers(pokemonTrainer, many=True)
            return Response(serializer.data)
        else:
            try:
                pokemonTrainer = PokemonTrainer.objects.get(pk=pk)
                serializer = PokeTrainerSerializers(pokemonTrainer)
                return Response(serializer.data)
            except:
                raise Http404
    def post(self, request, format = None):
        serializer = PokeTrainerSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pokemonTrainer = PokemonTrainer.objects.get(pk=pk)
            pokemonTrainer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        pokemonTrainer = PokemonTrainer.objects.get(pk=pk)
        serializer = PokeSerializers(pokemonTrainer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonTeam_APIView(APIView):
    """Class Pokemon Team to recive different web Methods (GET - POST - DELETE - PUT)
    If you don't have a id - Primarykey in Get method, you activate *Get ALL*
    """    
    def get(self, request, pk=None):
        if pk is None:
            pokemonTeam = PokemonTeam.objects.all()
            serializer = PokeTeamSerializer(pokemonTeam, many=True)
            return Response(serializer.data)
        else:
            try:
                pokemonTeam = PokemonTeam.objects.get(pk=pk)
                serializer = PokeTeamSerializer(pokemonTeam)
                return Response(serializer.data)
            except:
                raise Http404
            
    def post(self, request, format = None):
        serializer = PokeTeamSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pokemonTeam = PokemonTeam.objects.get(pk=pk)
            pokemonTeam.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.warning("Error: {}".format(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        pokemonTeam = PokemonTeam.objects.get(pk=pk)
        serializer = PokeTeamSerializer(pokemonTeam, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonTeamOnly_APIView(APIView):
    """Class Pokemon Team Only to recive different web Methods (GET - POST - DELETE - PUT)
    If you don't have a id - Primarykey in Get method, you activate *Get ALL*
    """
    def get(self, request, pk=None):
        if pk is None:
            pokemonTeamOnly = PokemonTeamOnly.objects.all()
            serializer = PokeTeamOnlySerializer(pokemonTeamOnly, many=True)
            return Response(serializer.data)
        else:
            try:
                pokemonTeamOnly = PokemonTeamOnly.objects.get(pk=pk)
                serializer = PokeTeamOnlySerializer(pokemonTeamOnly)
                return Response(serializer.data)
            except:
                raise Http404
            
    def post(self, request, format = None):
        serializer = PokeTeamOnlySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            pokemonTeamOnly = PokemonTeamOnly.objects.get(pk=pk)
            pokemonTeamOnly.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logging.warning("Error: {}".format(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        pokemonTeamOnly = PokemonTeamOnly.objects.get(pk=pk)
        serializer = PokeTeamOnlySerializer(pokemonTeamOnly, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)