from flask import Flask,render_template
import link_database as ldb

app = Flask(__name__)





liste_pokemon=[]
#ldb.reset()
#ldb.cree_la_table()
run=True
i=1
while run:
    try:
        print(i)
        ldb.pokemon(i)
        i+=1
    except:
        run=False

liste_pokemon=ldb.recuper_les_stats_des_pokemon()
@app.route('/')
def pokedex():  # put application's code here
    return render_template('base.html',pokemons=liste_pokemon)



if __name__ == '__main__':
    app.run()
