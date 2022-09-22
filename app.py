from flask import Flask,render_template
import link_database as ldb
import requests
app = Flask(__name__)




class pokemon:
    def __init__(self,id):
        self.id = id
        self.getpokemon = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(self.id)).json()
        self.name= self.getpokemon["name"]
        self.type_pokemon = self.getpokemon["types"][0]["type"]["name"]
        if len(self.getpokemon["types"]) > 1:
            self.type_pokemon2 = self.getpokemon["types"][1]["type"]["name"]
        else:
            self.type_pokemon2 = None
        self.image = self.getpokemon["sprites"]["front_default"]
        self.image_shiny = self.getpokemon["sprites"]["front_shiny"]
        self.hp = self.getpokemon["stats"][0]["base_stat"]
        self.attack = self.getpokemon["stats"][1]["base_stat"]
        self.defense = self.getpokemon["stats"][2]["base_stat"]
        self.speed = self.getpokemon["stats"][5]["base_stat"]

        print(self.type_pokemon)
    def retourne_les_stats(self):
        return {"id":id,"name":self.name,"type":self.type_pokemon,"hp":self.hp,"attack":self.attack,"defense":self.defense,"speed":self.speed}
liste_pokemon = []
for i in range(10):
    liste_pokemon.append(pokemon(i+1).retourne_les_stats())


@app.route('/')
def pokedex():  # put application's code here
    return render_template('base.html',pokemons=liste_pokemon)



if __name__ == '__main__':
    app.run()
