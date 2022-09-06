from django.contrib import admin
from .models import Pokemon, PokemonTrainer, PokemonTeam, PokemonTeamOnly

### ADd post to register in Admin Page
admin.site.register(Pokemon)
admin.site.register(PokemonTeam)
admin.site.register(PokemonTrainer)
admin.site.register(PokemonTeamOnly)
