import pokepy
import sqlite3
import pandas as pd
from pandas import DataFrame


conn = sqlite3.connect('pokemonDb.db')
pokemon_df = pd.read_sql("select * from pokemon", conn, index_col=None)

# 1. mean/avg weight of pokemon:
print("Average Weight:", pokemon_df['weight'].mean())


# 2. Highest accuracy move by Pokemon type
moves_df = pd.read_sql("select * from move;", conn, index_col=None)
max_accuracy = moves_df.drop(columns=['id']).groupby(['type']).max()

print("\n\nMaximim accuracy by pokemon types:\n")
print(max_accuracy)


# 3. Count and sort data from most to least moves by pokemon
pokemon_df['moves_list'] = pokemon_df['moves'].str.split(',')
pokemon_df['num_moves'] = pokemon_df['moves_list'].str.len()
print("\n\nCount the number of moves by Pokemon and order from greatest to least")
print(pokemon_df.sort_values('num_moves', ascending=False))

# Pokemon with the maximum moves
max_moves_row = pokemon_df[ pokemon_df['num_moves'] == max(pokemon_df['num_moves']) ]
print('\n\nPokemon with most moves:', max_moves_row['name'].to_string(index=False),\
             '\nNumber of moves:', max_moves_row['num_moves'].to_string(index=False))

