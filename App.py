import sys
import mysql.connector
from Query import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QWidget, \
    QComboBox, QFileDialog, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush, QPalette



class MainWindow(QWidget):
    """
    Classe qui permet de réaliser des actions dans la fenêtre
    """
    def __init__(self, cnx):
        self.cnx = cnx  # connector mysql
        self.cursor = self.cnx.cursor()
        super().__init__()
        # liste qui contient les query à exécuter
        self.listQueries = ["La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement.",
                           "La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.",
                            "La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments.",
                            "Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) aprés une date donnée, par exemple en cas de rappel de produit pour lot contaminé.",
                            "Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patients suive bien un traitement chronique.",
                            "La liste des médecins ayant prescrit des médicaments ne relevant pas de leur spécialité.",
                            "Pour chaque décennie entre 1950 et 2020, (1950−59, 1960−69, ...), le médicament le plus consommé par des patients nés durant cette décennie.",
                            "Quelle est la pathologie la plus diagnostiquée ?",
                            "Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament.",
                            "La liste de médicament n’étant plus prescrit depuis une date spécifique.",
                            "Inscrire un patient ou médecin ou pharmacien",
                            "se connecter en tant que patient",
                            "faire une recherche"]
        self.listButton = []  # liste qui contient les boutons du menu
        self.listParameter = []  # liste qui contient les paramètres de la requête
        self.listInputButton = []  #
        self.pageWidget = []
        self.labelWidget = []
        self.NISS = 0
        self.initUI()
        self.width = 1950
        self.height = 980
        self.nbrParameters = 0
        self.position = 0

    def initUI(self):
        """
        méthode qui initialise la fenêtre
        :return: void
        """
        self.setWindowTitle("Info-H303 : Base de données")
        self.setGeometry(5, 40, 1950, 980)
        self.createButton()


    def createButton(self):
        """
        méthode qui crée les boutons du menu principal
        :return: void
        """
        for i in range(len(self.listQueries)):  # pour chaque élément de la liste de requêtes
            button = QPushButton(self.listQueries[i], self)   # création d'un bouton
            button.setToolTip('Choisir cette requête')
            button.resize(1500,50)
            button.move(200,40+i*70)
            button.clicked.connect(self.onClick)
            self.listButton.append(button)

    def getNbrParameters(self, queryNbr):
        """
        méthode qui permet de déterminer combien de paramètres une requête a besoin
        :param queryNbr: numéro de la requête
        :return: un entier qui indique le nombre de paramètres dont a besoin la requête
        """
        if queryNbr == 1 or queryNbr == 10:
            return 1
        elif queryNbr == 4 or queryNbr == 5:
            return 2
        elif queryNbr == 3 or queryNbr == 6 or queryNbr == 7 or queryNbr == 8 or queryNbr == 9 or queryNbr == 2:
            return 0



    def hideButton(self):
        """
        méthode qui cache tout les boutons du menu principal
        :return: void
        """
        for i in range(len(self.listButton)):
            self.listButton[i].hide()

    def showButton(self):
        """
        methode qui affiche tous les boutons du menu principal
        :return: void
        """
        for i in range(len(self.listButton)):
            self.listButton[i].show()

    def inputParameter(self):
        label = QLabel("Entrez vos paramètres :", window)
        label.move(150,35)
        self.pageWidget.append(label)
        for i in range(self.nbrParameters):
            inputBox = QLineEdit(self)
            inputBox.resize(450,50)
            inputBox.move(200, 70+i*70)
            inputBox.show()
            self.listInputButton.append(inputBox)
        button = QPushButton('ok', self)
        button.setToolTip('Envoyer les paramètres')
        button.move(200, 700)
        button.show()
        button.clicked.connect(self.doneClick)
        self.listInputButton.append(button)
        self.showPage()



    def doneClick(self):
        self.deletePage()
        for i in range(len(self.listInputButton) - 1):
            self.listParameter.append(self.listInputButton[i].text())
            self.listInputButton[i].deleteLater()
        self.listInputButton[len(self.listInputButton) - 1].deleteLater()
        self.listInputButton.clear()
        query = Query(self.cnx, self.position, self.nbrParameters)
        query = Query(self.cnx, self.position, self.nbrParameters)
        self.drawAnswer(query.execute(self.listParameter))

    def drawAnswer(self, listAnswer):
        label = QLabel("Vos résultats :", window)
        self.pageWidget.append(label)
        label.move(150, 7)
        label.show()
        for i in range(len(listAnswer)):
            buf =''
            for j in range(len(listAnswer[i])):
                buf = buf + str(listAnswer[i][j]) + ', '
            label = QLabel(buf, window)
            self.pageWidget.append(label)
            label.move(100 +330 * ((70+i*30)//750), (70+i*30)%750)
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 800)
        self.pageWidget.append(button)
        self.showPage()

    def deleteLabels(self):
        for label in self.labelWidget:
            label.deleteLater()
        self.labelWidget.clear()

    def deletePage(self):
        self.deleteLabels()
        for elem in self.pageWidget:
            elem.deleteLater()
        self.pageWidget.clear()

    def showPage(self):
        for elem in self.pageWidget:
            elem.show()
        for label in self.labelWidget:
            label.show()


    def returnMenu(self):
        self.deletePage()
        self.showButton()

    def executeChange(self):
        toChange = self.pageWidget[1].currentText()
        newValue = self.pageWidget[0].text()
        if toChange == 'Pharmacien':
            self.cursor.execute("UPDATE ProjetDB.patient SET inami_pharmacien = %s WHERE NISS = %s", (newValue, self.NISS,))
        else:
            self.cursor.execute("UPDATE ProjetDB.patient SET inami_medecin = %s WHERE NISS = %s", (newValue, self.NISS,))
        self.cnx.commit()


    def modifyData(self):
        """
        méthode qui permet de modifier son médecin ou pharmacien de référence
        :return: void
        """
        self.deletePage()
        dataToChange = QComboBox(self)
        dataToChange.addItem("Médecin")
        dataToChange.addItem("Pharmacien")
        dataToChange.resize(200,50)
        dataToChange.move(250,120)
        label = QLabel("Choissisez quelles données vous voulez modifier puis Entrez le nouvel INAMI de votre médecin ou pharmacien :", window)
        label.move(150, 70)
        inputBox = QLineEdit(self)
        inputBox.resize(200, 50)
        inputBox.move(250, 200)
        sendButton = QPushButton('ok', self)
        sendButton.setToolTip('Envoyer les paramètres')
        sendButton.clicked.connect(self.executeChange)
        sendButton.move(450, 700)
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 700)
        self.pageWidget.append(inputBox)
        self.pageWidget.append(dataToChange)
        self.pageWidget.append(label)
        self.pageWidget.append(sendButton)
        self.pageWidget.append(button)
        self.showPage()

    def showDiagnostique(self):
        """
        méthode qui affiche les diagnostiques d'un patient connecté
        :return: void
        """
        self.deletePage()
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 700)
        # selection de la date de diagnostique et du nom de la pathologie pour le patient connecté
        self.cursor.execute("SELECT date_diagnostic, pathology FROM ProjetDB.diagnostiques WHERE NISS = %s", (self.NISS,))
        label = QLabel("Vos diagnostiques", window)
        label.move(200, 100)
        self.pageWidget.append(label)
        i =0
        for elem in self.cursor:
            # affichage des résultats
            buff = 'Nom de la pathologie : ' + elem[1] + " et date de diagnostique " + str(elem[0])
            label = QLabel(buff, window)
            label.move(200, 150 + i * 20)
            self.pageWidget.append(label)
            i += 1
        self.pageWidget.append(button)
        self.showPage()

    def showTraitement(self):
        """
        méthode qui affiche tous les traitements d'un patient
        :return: void
        """
        self.deletePage()
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 700)
        self.pageWidget.append(button)
        # selection de la date de prescription et du nom commercial des médicaments que prend le patient
        self.cursor.execute("SELECT date_prescription, medicament_nom_commercial FROM ProjetDB.dossiers_patients WHERE NISS_patient = %s",
                            (self.NISS,))
        label = QLabel("Vos traitements :", window)
        label.move(200, 100)
        i = 0
        for elem in self.cursor:
            # affichage des traitements
            buff = 'Nom du médicament : ' + elem[1]+ " et date de prescription "+ str(elem[0])
            label = QLabel(buff, window)
            label.move(200, 150 + i * 20)
            self.pageWidget.append(label)
            i += 1
        self.pageWidget.append(label)
        self.showPage()


    def accountAction(self):
        """
        méthode qui montre les actions qu'un utilisateur connecté peut réaliser
        :return: void
        """
        self.deletePage()
        changeReference = QPushButton('changer votre médecin/pharmacien', self)
        changeReference.setToolTip('choisir cette option')
        changeReference.clicked.connect(self.modifyData)
        changeReference.resize(350, 50)
        changeReference.move(200, 400)
        viewDiagno = QPushButton('consulter vos informations médicales', self)
        viewDiagno.setToolTip('choisir cette option')
        viewDiagno.clicked.connect(self.showDiagnostique)
        viewDiagno.resize(350, 50)
        viewDiagno.move(580, 400)
        viewTraite = QPushButton('consulter vos traitements', self)
        viewTraite.setToolTip('choisir cette option')
        viewTraite.clicked.connect(self.showTraitement)
        viewTraite.resize(350,50)
        viewTraite.move(960, 400)
        self.pageWidget.append(changeReference)
        self.pageWidget.append(viewDiagno)
        self.pageWidget.append(viewTraite)
        self.showPage()


    def connectionButton(self):
        """
        méthode qui vérifie que le compte existe lors d'une connection
        :return: void
        """
        NISSPatient = int(self.pageWidget[1].text())  # récupère le NISS du patient
        self.cursor.execute("SELECT * FROM ProjetDB.patient WHERE NISS = %s", (NISSPatient,))  # recherche et selection dans la DB
        result = self.cursor.fetchone()
        if result:   # si on trouve le NISS
            self.NISS = NISSPatient
            self.accountAction()  # affichage des actions réalisables lorsqu'on est connecté


    def connection(self):
        """
        méthode qui permet de se connecter
        :return: void
        """
        self.hideButton()
        label = QLabel("Entrer votre NISS :", window)
        label.move(150, 70)
        inputBox = QLineEdit(self)
        inputBox.resize(450, 50)
        inputBox.move(200, 100)
        button = QPushButton('ok', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.connectionButton)
        button.move(200, 700)
        self.pageWidget.append(label)
        self.pageWidget.append(inputBox)
        self.pageWidget.append(button)
        self.showPage()

    def selectionChanged(self):
        """
        méthode qui permet de faire apparaitre le bon nombre de innputbox selon l'ajout que lon veut faire
        :return: void
        """
        # détermination du nombre de paramètres selon la table dans laquelle ajouter.
        if self.pageWidget[0].currentText() == "Patient":
            iter = 9
        elif self.pageWidget[0].currentText() == "Médecin":
            iter = 5
        else:
            iter = 4
        if len(self.pageWidget) != iter+4:
            # création ou suppression de widgets pour avoir le bon nombre d'inputbox
            if len(self.pageWidget) < iter+4:
                for i in range(len(self.pageWidget), iter+4):
                    inputBox = QLineEdit(self)
                    inputBox.resize(450,50)
                    inputBox.move(200, 70+(i-2)*70)
                    self.pageWidget.append(inputBox)
            elif len(self.pageWidget) > iter+4:
                for i in range(iter+4,len(self.pageWidget)):
                    self.pageWidget[i].deleteLater()
                self.pageWidget = self.pageWidget[:iter+4]
        # création des bon labels et affichage de la page
        self.deleteLabels()
        self.createLabels(iter)
        self.showPage()

    def createLabels(self, requete):
        """
        méthode qui crée les labels nécessaires pour l'insertion
        :param requete: permet de determiner quel labels sont nécessaires
        :return: void
        """
        if requete == 4:
            # labels nécessaire pour pharmacien
            labels = ["Inami", "mail", "nom", "téléphone"]
        elif requete == 5:
            # labels nécessaire pour médecin
            labels = ["Inami", "mail", "nom","spécialité", "téléphone"]
        else:
            # label nécessaire pour patient
            labels = ["NISS", "date de naissance", "genre","Inami du médecin","Inami du pharmacien","mail","nom", "prénom", "téléphone"]
        for i in range(len(labels)):
            # creation du label et ajout à la liste
            label = QLabel(labels[i], self)
            label.move(80,225+i*70)
            self.labelWidget.append(label)


    def insertData(self):
        """
        méthode qui réalise la requête sql qui ajpoute un élément dans la DB
        :return: void
        """
        ValueToInsert = []
        for i in range(4, len(self.pageWidget)):
            ValueToInsert.append(self.pageWidget[i].text())   # récupération des paramètre
        if self.pageWidget[0].currentText() =="Patient":   # selon la table dans laquelle on veut ajouter
            # transformation en bon type pour certains paramètres
            ValueToInsert[0] = int(ValueToInsert[0])
            ValueToInsert[2] = int(ValueToInsert[2])
            ValueToInsert[8] = int(ValueToInsert[8])
            ValueToInsert[3] = int(ValueToInsert[3])
            # réalisation de la requête
            self.cursor.execute("INSERT INTO ProjetDB.patient (NISS, date_de_naissance, genre,inami_medecin, inami_pharmacien, mail, nom, prenon, telephone) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", ValueToInsert)
        elif self.pageWidget[0].currentText() =="Médecin":
            ValueToInsert[0] = int(ValueToInsert[0])
            ValueToInsert[4] = int(ValueToInsert[4])
            self.cursor.execute("INSERT INTO ProjetDB.medecins (inami, mail, nom, specialite,telephone) VALUES(%s,%s,%s,%s,%s)",ValueToInsert)
        else:
            ValueToInsert[0]= int(ValueToInsert[0])
            ValueToInsert[3] = int(ValueToInsert[3])
            self.cursor.execute("INSERT INTO ProjetDB.pharmacien (inami, mail, nom, telephone) VALUES(%s,%s,%s,%s)", ValueToInsert)
        cnx.commit()   # commit des changements

    def addInfo(self):
        """
        méthode qui permet d'ajouter un élément à la DB
        :return: void
        """
        self.hideButton()
        label = QLabel("Choississez quelle information vous voulez ajouter :", window)
        label.move(150, 70)
        # Choix de l'élément qu'on veut rajouter
        comboBox = QComboBox(self)
        comboBox.addItem("Patient")
        comboBox.addItem("Médecin")
        comboBox.addItem("Pharmacien")
        comboBox.move(200,150)
        comboBox.resize(200, 50)
        comboBox.currentIndexChanged.connect(self.selectionChanged)
        # bouton qui valide l'ajout de l'élément et bouton permet de retourner au menu
        sendButton = QPushButton('ok', self)
        sendButton.setToolTip('Envoyer les paramètres')
        sendButton.clicked.connect(self.insertData)
        sendButton.move(450, 850)
        sendButton.resize(200, 50)
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 850)
        # rajout de tous les widgets à la liste
        self.pageWidget.append(comboBox)
        self.pageWidget.append(sendButton)
        self.pageWidget.append(button)
        self.pageWidget.append(label)
        self.showPage()   # affichage de  la page


    def search(self):
        specialite = self.pageWidget[3].text()
        print(specialite)
        self.deleteLabels()
        if self.pageWidget[2].currentText() == "Médecin":
            self.cursor.execute("SELECT * FROM ProjetDB.medecins WHERE specialite = %s",(specialite,))  # recherche et selection dans la DB
        else:
            self.cursor.execute("SELECT * FROM ProjetDB.medicaments WHERE système_anatomique = %s",(specialite,))  # recherche et selection dans la DB
        i =0
        for selected in self.cursor:
            buf = ""
            for elem in selected:
                if elem != None:
                    buf = buf + str(elem) + ",  "
            label = QLabel(buf, window)
            label.move(200, 200 + i * 30)
            i +=1
            self.labelWidget.append(label)
        self.showPage()


    def makeASearch(self):
        """
        méthode qui permet de réaliser une recherche à facette
        :return: void
        """
        self.hideButton()
        # Création du bon ton de retour et du bouton pour valider
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 850)
        sendButton = QPushButton('ok', self)
        sendButton.setToolTip('Envoyer les paramètres')
        sendButton.clicked.connect(self.search)
        sendButton.move(450, 850)
        sendButton.resize(200, 50)
        self.pageWidget.append(sendButton)
        self.pageWidget.append(button)
        # Création de la combo box qui permet de choisir quelle recherche faire
        comboBox = QComboBox(self)
        comboBox.addItem("médicament")
        comboBox.addItem("Médecin")
        comboBox.move(50, 100)
        comboBox.resize(200, 50)
        self.pageWidget.append(comboBox)
        # input box qui permet de filtrer la recherche
        inputBox = QLineEdit(self)
        inputBox.resize(200, 50)
        inputBox.move(270, 100)
        self.pageWidget.append(inputBox)
        self.showPage()



    def onClick(self):
        """
        méthode qui traite le fait d'appuyer sur un des boutons du menu principal
        :return: void
        """
        sender = self.sender()                                            # récupère l'objet sur lequel on a cliqué
        self.position = int((sender.pos().y()-40)//70+1)                  # récupère l'indice de la position de l'ojet
        self.nbrParameters = self.getNbrParameters(self.position)         # détermine le nombre de paramètre de la requête
        # S'il n' y a pas de paramètre, exécution de la requête et affichage de la réponse
        if self.position < 11 and self.nbrParameters == 0:
            self.hideButton()
            query = Query(self.cnx, self.position, self.nbrParameters)
            self.drawAnswer(query.execute(self.listParameter))
        elif self.position < 11:
            self.hideButton()
            self.inputParameter()    # demande de paramètre
        else:
            if self.position == 11:
                self.addInfo()       # requête qui permet d'ajouter un élément à la DB
            elif self.position == 12:
                self.connection()    # requête qui permet de se connecter
            else:
                self.makeASearch()   # recherche à facette


if __name__ == '__main__':
    """Fonction principale qui lance le code"""
    app = QApplication(sys.argv)
    cnx = mysql.connector.connect(user='root', password='passpass',
                                  host='localhost',
                                  database='ProjetDB')
    window = MainWindow(cnx)
    window.show()
    sys.exit(app.exec_())