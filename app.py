from flask import Flask,render_template
import link_database as ldb
app = Flask(__name__)




class pokemon:
    def __init__(self,name,type,hp,attack,defense,speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.image= "static/pokemon img/"+name+".png"
    def retourne_les_stats(self):
        return {"name":self.name,"type":self.type,"hp":self.hp,"attack":self.attack,"defense":self.defense,"speed":self.speed,"image":self.image}
liste_pokemon = []
for p in ldb.recuper_les_stats_des_pokemon():
    poke=pokemon(p[0],p[1],p[2],p[3],p[4],p[5])
    liste_pokemon.append(poke.retourne_les_stats())

@app.route('/')
def pokedex():  # put application's code here
    return render_template('base.html',pokemons=liste_pokemon)



if __name__ == '__main__':
    app.run()
