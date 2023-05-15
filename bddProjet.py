import mysql.connector
from Query import *



def main():
    # se connecter a la base de donnees
    cnx = mysql.connector.connect(user='guest', password='passpass',
                                host='localhost',
                                database='bddProjet')
    res = True
    while res:
        buf = input("voulez-vous arretez votre recherche? Y or N")
        if(buf == 'Y'):
            res = False
        else:
            buf = input("Quelles est votre requete ?\n")
            requete = Query(cnx, buf)
            requete.execute()

    # fermer la connexion à la base de données
    cnx.close()

if __name__ == "__main__":  # code principale
    main()