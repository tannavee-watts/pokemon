import pokepy
import sqlite3
import re

REPLACE_UNWANTED_CHARS = r'<|>|Named_API_Resource \| '

conn = sqlite3.connect('pokemonDb.db')
cur = conn.cursor()
client = pokepy.V2Client()


insertPokemonSql = ''' INSERT OR IGNORE INTO pokemon(id,name,height,weight,moves,types) VALUES(?,?,?,?,?,?) '''
insertMoveSql = '''INSERT OR IGNORE INTO move(id,name,accuracy,type) VALUES(?,?,?,?)'''

pokemon_list = []
pokemon_moves_list = []

# Create a list of the 1st 15 pokemon from the Pokemon API
for i in range(1,16):
    p = client.get_pokemon(i)
    pokemon_list.append(p)

# Insert cleaned/transformed rows into dabase tables
for pokemon in pokemon_list:
    type_str = ''
    moves_str = ''

    # Create a readable/cleaned string value from PokemonType
    for t in pokemon.types:
        type_str += re.sub(REPLACE_UNWANTED_CHARS, '', str(t.type)) + ","

    if type_str[-1:] == ',':
        type_str = type_str[:-1]

    # Create a readable/cleaned string value from PokemonMove
    for move in pokemon.moves:
        cleaned_move = re.sub(REPLACE_UNWANTED_CHARS, '', str(move.move))
        moves_str += cleaned_move + ","

        if move.move not in pokemon_moves_list:
            pokemon_moves_list.append(cleaned_move)
    
    if moves_str[-1:] == ',':
        moves_str = moves_str[:-1]
    
    row = (pokemon.id, pokemon.name, pokemon.height, pokemon.weight, moves_str, type_str)

    cur.execute(insertPokemonSql, row)
    conn.commit()

for m in pokemon_moves_list:
    move = client.get_move(m)
    row = (move.id, move.name, move.accuracy, re.sub(REPLACE_UNWANTED_CHARS, '', str(move.type)))
    cur.execute(insertMoveSql, row)
    conn.commit()