from flask import Flask,render_template
import link_database as ldb

app = Flask(__name__)





liste_pokemon = []
ldb.reset()
ldb.cree_la_table()
for i in range(1,10):
    liste_pokemon.append(ldb.pokemon(i))
    print(liste_pokemon[i-1].name)
    print(liste_pokemon[i-1].type_pokemon)
    print(liste_pokemon[i-1].hp)
    print(liste_pokemon[i-1].attack)
    print(liste_pokemon[i-1].defense)
    print(liste_pokemon[i-1].speed)
    print(liste_pokemon[i-1].image)
    print(liste_pokemon[i-1].image_shiny)
@app.route('/')
def pokedex():  # put application's code here
    return render_template('base.html',pokemons=liste_pokemon)



if __name__ == '__main__':
    app.run()
