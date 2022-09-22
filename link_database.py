from sqlite3 import *
lien_vers_le_fichier ="database/pokedex.db"
import requests
class pokemon:
    def __init__(self,id):
        self.id = id
        self.getpokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(self.id)).json()
        self.getpokemon_fr=requests.get("https://pokebuildapi.fr/api/v1/pokemon/"+str(self.id)).json()
        self.name=self.getpokemon_fr["name"]
        self.type_pokemon=self.getpokemon_fr["apiTypes"]
        #self.type_pokemon = self.getpokemon["types"][0]["type"]["name"]
        self.type_pokemon1=self.type_pokemon[0]["name"]
        if len(self.type_pokemon) > 1:
            self.type_pokemon2 = self.type_pokemon[1]["name"]
        else:
            self.type_pokemon2 = " "

        self.image = self.getpokemon["sprites"]["front_default"]
        self.image_shiny = self.getpokemon["sprites"]["front_shiny"]
        self.hp = self.getpokemon["stats"][0]["base_stat"]
        self.attack = self.getpokemon["stats"][1]["base_stat"]
        self.defense = self.getpokemon["stats"][2]["base_stat"]
        self.speed = self.getpokemon["stats"][5]["base_stat"]

        ajouter_un_pokemon(self.id,self.name,self.type_pokemon1,self.type_pokemon2,self.hp,self.attack,self.defense,self.speed,self.image,self.image_shiny)
#cree la table
def cree_la_table():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS pokemon (id INTEGER PRIMARY KEY,name TEXT,type_pokemon1 TEXT,type_pokemon2 TEXT,hp INTEGER,attack INTEGER,defense INTEGER,speed INTEGER,image TEXT,image_shiny TEXT)")
    conn.commit()
#reset la table
def reset():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS pokemon")
    conn.commit()
def recuper_les_stats_des_pokemon():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("SELECT * FROM pokemon")
    return c.fetchall()

def ajouter_un_pokemon(id,name,type_pokemon1,type_pokemon2,hp,attack,defense,speed,image,image_shiny):
    conn = connect(lien_vers_le_fichier)
    c = conn.cursor()
    c.execute("INSERT INTO pokemon VALUES (?,?,?,?,?,?,?,?,?,?)",(id,name,type_pokemon1,type_pokemon2,hp,attack,defense,speed,image,image_shiny))
    conn.commit()

def supprimer_un_pokemon(name):
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("DELETE FROM pokemon WHERE name = ?",(name,))
    conn.commit()