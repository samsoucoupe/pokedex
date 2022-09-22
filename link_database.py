from sqlite3 import *
lien_vers_le_fichier ="database/pokedex.db"
#cree la table
def cree_la_table():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("CREATE TABLE pokemon (name TEXT, type TEXT, hp INTEGER, attack INTEGER, defense INTEGER, speed INTEGER)")
    conn.commit()

def recuper_les_stats_des_pokemon():
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("SELECT * FROM pokemon")
    return c.fetchall()

def ajouter_un_pokemon(name,type,hp,attack,defense,speed):
    conn = connect(lien_vers_le_fichier)
    c = conn.cursor()
    c.execute("INSERT INTO pokemon VALUES (?,?,?,?,?,?)",(name,type,hp,attack,defense,speed))
    conn.commit()


def supprimer_un_pokemon(name):
    conn = connect(lien_vers_le_fichier )
    c = conn.cursor()
    c.execute("DELETE FROM pokemon WHERE name = ?",(name,))
    conn.commit()