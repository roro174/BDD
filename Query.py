class Query:
    def __init__(self, cnx, queryType):
        self.cnx = cnx
        self.queryType = queryType
    

    def execute(self, parametre):
        match self.queryType:
            case "1":
                with open('QueriesFile/query1.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "2":
                with open('QueriesFile/query2.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)                   
            case "3":
                with open('QueriesFile/query3.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "4":
                with open('QueriesFile/query4.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "5":
                with open('QueriesFile/query5.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "6":
                with open('QueriesFile/query6.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "7":
                with open('QueriesFile/query7.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "8":
                with open('QueriesFile/query8.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "9":
                with open('QueriesFile/query9.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case "10":
                with open('QueriesFile/query10.sql', 'r') as f:
                    script = f.read()
                    script = script.replace('%s', parametre)
            case _:
                if(self.queryType == "insérer"):
                    cursor = self.cnx.cursor()
                    query = ("SELECT nom, prenom FROM table")
                    cursor.execute(query)
                elif(self.queryType == "se connecter"):
                    cursor = self.cnx.cursor()
                    query = ("SELECT nom, prenom FROM table")
                    cursor.execute(query)
        cursor = self.cnx.cursor()
        cursor.execute(script)
        resultats = cursor.fetchall()
        for resultat in resultats:
            print(resultat[0], resultat[1])
            #for (nom, prenom) in cursor:
                # print("{} {}".format(nom, prenom))"""

                
