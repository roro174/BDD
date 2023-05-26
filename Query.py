"""
*noms: Fatima Ouchen, Lina Mahyo, Rodolphe Prévot
*date: 26/05/2023
*contenu: projet d'os 2 qui traite: des requêtes à faire sur une base de données/une division en serveur et clients, chacun pris en charge par un thread/ bash
"""


class Query:
    """
    Classse qui réalise les requêtes qui se trouve dans un fichier
    """
    def __init__(self, cnx, queryType, nbrParameter):
        """
        initialisation de la classe
        :param cnx: connector mysql
        :param queryType: int qui détermine quelle requête exécuter
        :param nbrParameter: le nombre de paramètres de la requête
        """
        self.cnx = cnx
        self.queryType = queryType
        self.nbrParameter = nbrParameter

    def splitRequet(self, requet):
        """
        méthode qui divise la requête s'il y a plusieurs lignes
        :param requet: le contenu de la requête
        :return: une liste de requête
        """
        splitreq = requet.split(";")
        for elem in splitreq:
            elem = elem + ";"
        return splitreq

    def execute(self, parametre):
        """
        méthode qui réalise la requête
        :param parametre: liste de paramètre pour la requête
        :return: liste avec les résultats
        """
        cursor = self.cnx.cursor()
        match self.queryType:   # switch case por trouver le bon fichier
            case 1:
                with open('QueriesFile/query1.sql', 'r') as f:
                   script = f.read()
            case 2:
                with open('QueriesFile/query2.sql', 'r') as f:
                    script = f.read()
            case 3:
                with open('QueriesFile/query3.sql', 'r') as f:
                    script = f.read()
            case 4:
                with open('QueriesFile/query4.sql', 'r') as f:
                    script = f.read()
            case 5:
                with open('QueriesFile/query5.sql', 'r') as f:
                    script = f.read()
            case 6:
                with open('QueriesFile/query6.sql', 'r') as f:
                    script = f.read()
            case 7:
                with open('QueriesFile/query7.sql', 'r') as f:
                    script = f.read()
            case 8:
                with open('QueriesFile/query8.sql', 'r') as f:
                    script = f.read()
            case 9:
                with open('QueriesFile/query9.sql', 'r') as f:
                    script = f.read()
            case 10:
                with open('QueriesFile/query10.sql', 'r') as f:
                    script = f.read()
            case _:
                return
        # remplacement des paramètres dans la requête
        for i in range(self.nbrParameter):
            replaceValue = '$' + str(i+1)
            script = script.replace(replaceValue, parametre[i])
        splitreq = self.splitRequet(script)
        for req in splitreq:
            cursor.execute(req)   # exécution de chaque ligne
        retValue = []
        # récupération des résultats
        for x in cursor:
            retValue.append(x)

        return retValue

