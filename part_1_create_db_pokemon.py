import sqlite3


conn = sqlite3.connect('pokemonDb.db')
c = conn.cursor()

c.execute('''CREATE TABLE POKEMON
             (
                [id] integer PRIMARY KEY,
                [name] text,
                [height] integer,
                [weight] integer,
                [moves] text,
                [types] text
             )''')


c.execute('''CREATE TABLE MOVE
             (
                [id] integer PRIMARY KEY,
                [name] text,
                [accuracy] integer,
                [type] text
             )''')
conn.commit()