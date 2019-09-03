# pokemon_metrics

This repository utilizes the [PokeAPI](https://pokeapi.co/docs/v2.html#info) with the [Pokepy]((https://pokeapi.github.io/pokepy/)) library to answer the following questions:

1. What is the average weight of the pokemon by Pokemon type?
2. List the highest accuracy move by Pokemon type
3. Count the number of moves by Pokemon and order from greatest to least 

## Dependencies:
- [pokepy](https://pokeapi.github.io/pokepy/)
- [sqlite3](https://docs.python.org/2/library/sqlite3.html)
- [pandas](https://pandas.pydata.org/)
- [re](https://docs.python.org/3/library/re.html)

## Contents
1. [part_1_create_db_pokemon.py](https://github.com/tannavee-watts/pokemon_metrics/blob/master/part_1_create_db_pokemon.py): Creates two tables in a sqlite database (`pokemon` and `move`)
2. [part_2_insert__into_table_pokemon.py](https://github.com/tannavee-watts/pokemon_metrics/blob/master/part_2_insert__into_table_pokemon.py): Reads information from the PokeAPI and writes to the two sqlite database tables defined in part 1.
3. [part_3_pokemon_find_results.py](https://github.com/tannavee-watts/pokemon_metrics/blob/master/part_3_pokemon_find_results.py): Reads data from sqlite database into dataframes and finds information required (answers questions 1,2, and 3 mentioned above).
4. [requirements.txt](https://github.com/tannavee-watts/pokemon_metrics/blob/master/requirements.txt): dependencies to be installed/libraries used in this project
5. [pokemonDb.db](https://github.com/tannavee-watts/pokemon_metrics/blob/master/pokemonDb.db): sqlite database
6. results.txt: Contains the output from running `part_3_pokemon_find_results.py`