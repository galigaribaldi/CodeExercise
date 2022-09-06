from django.contrib import admin
from django.urls import path
from Pokeapi.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('v1/Pokemon/<int:pk>', Pokemon_APIView.as_view()),
    path('v1/Pokemon', Pokemon_APIView.as_view()),
    
    path('v1/PokeTraining/<int:pk>', PokemonTrainer_APIView.as_view()),
    path('v1/PokeTraining', PokemonTrainer_APIView.as_view()),
    
    path('v1/PokeTeam/<int:pk>', PokemonTeam_APIView.as_view()),
    path('v1/PokeTeam', PokemonTeam_APIView.as_view()),
    
    path('v1/PokeTeamOnly/<int:pk>', PokemonTeamOnly_APIView.as_view()),
    path('v1/PokeTeamOnly', PokemonTeamOnly_APIView.as_view()),    
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
