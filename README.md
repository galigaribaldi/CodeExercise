# Code Excercise

## Primero pasos

Repositorio que contiene una API sobre pokemon hecha con Django y Postgres SQL.

Para poder correr el código correctamente, es necesario tener instalado python en su versión *python-3.9.13* o superior. Una vez instalada ésta versión del interprete, se debe ejecutar el siguiente comando para instalar las librerías necesarias:

```bash
pip install -r requiriments.txt
```

Éste comando nos ayudará a instalar las librerías necesarias para correr nuestro [código](https://github.com/galigaribaldi/CodeExercise/blob/main/requirements.txt). Acto siguiente ejecutar el siguiente comando para ejecutar el código:

```bash
python3 manage.py runserver
```

Nos desplegará una señal de aviso en nuestra consola, diciendonos que ya está ejecutándose nuestro proyecto.

## Descripción de la API

La API simula una pequeña BD sobre 4 elementos **Pokemon, Entrenadores Pokemon, Equipos Pokemon (Entrenadores), Equipos Pokemon (Sólo pokemons)**



### Uso de la API en Local

**Importante: Para poder hacer uso de ésta sección, el código debe estarse ejecutando de manera correcta en la máquina local**. De la misma forma, se debe revisar en que puerto - liga se está ejecutando el código; por lo regular se ejecuta en *localhost*, pero se recomienda checar. La descripción de las ligas (locales - **http://127.0.0.1:8000/**) se muestran a continuación



### Uso de la API en Heroku

**Importante: Para poder hacer uso de ésta sección, se debe tener conexión a internet para poder ejecutar las consultas, ya que estás se encuentran alojadas en el servidor de Heroku: https://code-excersice.herokuapp.com**. La descripción de las ligas se muestran a continuación



#### Pokemon

Obtener - Crear - Eliminar - Modificar la información relacionada con los pokemons

- **GET ALL**: Obtener todos los registros
  - Local: http://127.0.0.1:8000:8000/v1/Pokemon
  - Heroku: https://code-excersice.herokuapp.com/v1/Pokemon
- **GET BY ID**: Obtener un registro por su ID
  - Local: http://127.0.0.1:8000:8000/v1/Pokemon/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/Pokemon/{id}
- **POST**: Publica run nuevo registro de Pokemon
  - Local: http://127.0.0.1:8000:8000/v1/Pokemon
  - Heroku: https://code-excersice.herokuapp.com/v1/Pokemon
- **DELETE**: Eliminar un registro
  - Local: http://127.0.0.1:8000:8000/v1/Pokemon/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/Pokemon/{id}
- **PUT**: Modificar la información
  - Local: http://127.0.0.1:8000/v1/Pokemon/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/Pokemon/{id}

Estructura del Body json

```json
{
  "name": "Charizard",
	"growth_time": 10,
	"max_harvest": 20,
	"natural": "Fire",
	"preEvolution": "Charmander",
	"evolution": "",
	"natural_gift_power": 30,
	"size": 10,
	"smoothness": 220,
	"soil_dryness": 20,
	"potency": 10
}
```



#### Entrenadores Pokemon

Obtener - Crear - Eliminar - Modificar la información relacionada con los entrenadores Pokemons

- **GET ALL**: Obtener todos los registros
  - Local: http://127.0.0.1:8000:8000/v1/PokeTraining
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTraining
- **GET BY ID**: Obtener un registro por su ID
  - Local: http://127.0.0.1:8000:8000/v1/PokeTraining/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTraining/{id}
- **POST**: Publica run nuevo registro de Enrtrenador Pokemon
  - Local: http://127.0.0.1:8000:8000/v1/PokeTraining
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTraining
- **DELETE**: Eliminar un registro
  - Local: http://127.0.0.1:8000:8000/v1/PokeTraining/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTraining/{id}
- **PUT**: Modificar la información
  - Local: http://127.0.0.1:8000/v1/PokeTraining/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTraining/{id}

Estructura del Body json

```json
{
	"id": 1,
	"name": "Pepe",
	"age": 12.0,
	"origin_city": "Pueblo Paleta",
	"gender": "M",
	"region_name": "Oeste",
	"is_training": true,
	"pokemon": [
		1
	]
}
```



#### Equipos Pokemon (Entrenadores)

Obtener - Crear - Eliminar - Modificar la información relacionada con los equipos Pokemons

- **GET ALL**: Obtener todos los registros
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeam
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeam
- **GET BY ID**: Obtener un registro por su ID
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeam/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeam/{id}
- **POST**: Publica run nuevo registro de Pokemon
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeam
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeam
- **DELETE**: Eliminar un registro
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeam/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeam/{id}
- **PUT**: Modificar la información
  - Local: http://127.0.0.1:8000/v1/PokeTeam/{if}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeam/{id}

Estructura del Body json

```json
{
	"id": 1,
	"name": "Team 1",
	"origin_city": "Oeste",
	"region_name": "Oeste",
	"number_wins": 1,
	"pokemonTrainer": [
		1
	]
}
```



#### Equipos Pokemon (Sólo Pokemons)

Obtener - Crear - Eliminar - Modificar la información relacionada con los equipos Pokemons

- **GET ALL**: Obtener todos los registros
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeamOnly
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeamOnly
- **GET BY ID**: Obtener un registro por su ID
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeamOnly/{id}
  - Heroku:  https://code-excersice.herokuapp.com/v1/PokeTeamOnly/{id}
- **POST**: Publica run nuevo registro de Pokemon
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeamOnly
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeamOnly
- **DELETE**: Eliminar un registro
  - Local: http://127.0.0.1:8000:8000/v1/PokeTeamOnly/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeamOnly/{id}
- **PUT**: Modificar la información
  - Local: http://127.0.0.1:8000/v1/PokeTeamOnly/{id}
  - Heroku: https://code-excersice.herokuapp.com/v1/PokeTeamOnly/{id}

Estructura del Body json

```json
{
	"id": 4,
	"nameTeam": "",
	"onlyPokemon": true,
	"pokemon": [
		1
	]
}
```

