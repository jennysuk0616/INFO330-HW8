import sqlite3
import sys
import xml.etree.ElementTree as ET

# Incoming Pokemon MUST be in this format
#
# <pokemon pokedex="" classification="" generation="">
#     <name>...</name>
#     <hp>...</name>
#     <type>...</type>
#     <type>...</type>
#     <attack>...</attack>
#     <defense>...</defense>
#     <speed>...</speed>
#     <sp_attack>...</sp_attack>
#     <sp_defense>...</sp_defense>
#     <height><m>...</m></height>
#     <weight><kg>...</kg></weight>
#     <abilities>
#         <ability />
#     </abilities>
# </pokemon>

conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()

if len(sys.argv) < 2:
    print("You must pass at least one XML file name containing Pokemon to insert")
    sys.exit()

for i, arg in enumerate(sys.argv):

    if i == 0:
        continue

    try:
        tree = ET.parse(arg)
        root = tree.getroot()
    except ET.ParseError:
        print(f"Error parsing {arg}")
        continue

    name = root.find('name').text
    pokedex = root.get('pokedex')
    classification = root.get('classification')
    generation = root.get('generation')
    hp = int(root.find('hp').text)
    attack = int(root.find('attack').text)
    defense = int(root.find('defense').text)
    speed = int(root.find('speed').text)
    sp_attack = int(root.find('sp_attack').text)
    sp_defense = int(root.find('sp_defense').text)
    height = float(root.find('height/m').text)
    weight = float(root.find('weight/kg').text)

    abilities = []
    for ability in root.findall('abilities/ability'):
        abilities.append(ability.text)

    c.execute("SELECT COUNT(*) FROM pokemon WHERE name = ?", (name,))
    if c.fetchone()[0] > 0:
        print(f"{name} already exists in the database. Skipping.")
        continue

    c.execute("INSERT INTO pokemon (pokedex, name, classification, generation, hp, attack, defense, speed, sp_attack, sp_defense, height, weight) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
              (pokedex, name, classification, generation, hp, attack, defense, speed, sp_attack, sp_defense, height, weight))
    pokemon_id = c.lastrowid

    for ability in abilities:
        c.execute("INSERT INTO abilities (ability, pokemon_id) VALUES (?, ?)", (ability, pokemon_id))

    print(f"Inserted {name} into the database")

conn.commit()
conn.close()
