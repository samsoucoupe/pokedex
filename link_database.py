from sqlite3 import *
lien_vers_le_fichier ="database/pokedex.db"
import requests
class pokemon:
    def __init__(self,id):

        if recuper_id(id) == None:
            self.id = id
            self.getpokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(self.id)).json()
            self.getpokemon_fr=requests.get("https://pokebuildapi.fr/api/v1/pokemon/"+str(self.id)).json()
            self.name=self.getpokemon_fr["name"]
            self.type_pokemon=self.getpokemon_fr["apiTypes"]
            #self.type_pokemon = self.getpokemon["types"][0]["type"]["name"]
            self.type_pokemon1=self.type_pokemon[0]["name"]
            self.type_pokemon1_assests=self.type_pokemon[0]["image"]
            if len(self.type_pokemon) > 1:
                self.type_pokemon2 = self.type_pokemon[1]["name"]
                self.type_pokemon2_assests=self.type_pokemon[1]["image"]
            else:
                self.type_pokemon2 = "⠀"
                self.type_pokemon2_assests=" "

            self.image = self.getpokemon["sprites"]["front_default"]
            self.image_shiny = self.getpokemon["sprites"]["front_shiny"]
            self.hp = self.getpokemon["stats"][0]["base_stat"]
            self.attack = self.getpokemon["stats"][1]["base_stat"]
            self.defense = self.getpokemon["stats"][2]["base_stat"]
            self.speed = self.getpokemon["stats"][5]["base_stat"]

            ajouter_un_pokemon(self.id,self.name,self.type_pokemon1,self.type_pokemon2,self.type_pokemon1_assests,self.type_pokemon2_assests,self.hp,self.attack,self.defense,self.speed,self.image,self.image_shiny)

def recuper_les_stats_des_pokemon():
    liste_pokemon = []
    for i in rec_les_stats_des_pokemon():
        liste_pokemon.append({"id":i[0],"name":i[1],"type_pokemon1":i[2],"type_pokemon2":i[3],"type_pokemon1_assests":i[4],"type_pokemon2_assests":i[5],"hp":i[6],"attack":i[7],"defense":i[8],"speed":i[9],"image":i[10],"image_shiny":i[11]})
    return liste_pokemon
def cree_la_table():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS pokemon (id INTEGER PRIMARY KEY,name TEXT,type_pokemon1 TEXT,type_pokemon2 TEXT,type_assets_1 TEXT,type_assets_2 TEXT,hp INTEGER,attack INTEGER,defense INTEGER,speed INTEGER,image TEXT,image_shiny TEXT)")
    conn.commit()
#reset la table
def reset():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS pokemon")
    conn.commit()
def rec_les_stats_des_pokemon():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("SELECT * FROM pokemon")
    return c.fetchall()

def ajouter_un_pokemon(id,name,type_pokemon1,type_pokemon2,type_assets_1,type_assets_2,hp,attack,defense,speed,image,image_shiny):
    conn = connect(lien_vers_le_fichier)
    c = conn.cursor()
    c.execute("INSERT INTO pokemon VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(id,name,type_pokemon1,type_pokemon2,type_assets_1,type_assets_2,hp,attack,defense,speed,image,image_shiny))
    conn.commit()

def supprimer_un_pokemon(name):
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("DELETE FROM pokemon WHERE name = ?",(name,))
    conn.commit()

def recuper_id(id):
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("SELECT id FROM pokemon WHERE id = ?",(id,))
    return c.fetchone()