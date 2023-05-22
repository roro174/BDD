import sys
import mysql.connector
from Query import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QWidget, \
    QComboBox, QFileDialog, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush, QPalette



class MainWindow(QWidget):
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()
        super().__init__()
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
                            "se connecter en tant que patient"]
        self.listButton = []
        self.listParameter = []
        self.listInputButton = []
        self.pageWidget = []
        self.NISS = 0
        self.initUI()
        self.width = 1950
        self.height = 980
        self.nbrParameters = 0
        self.position = 0

    def initUI(self):
        self.setWindowTitle("Info-H303 : Base de données")
        self.setGeometry(5, 40, 1950, 980)
        self.createButton()


    def createButton(self):
        for i in range(len(self.listQueries)):
            button = QPushButton(self.listQueries[i], self)
            button.setToolTip('Choisir cette requête')
            button.resize(1500,50)
            button.move(200,70+i*70)
            button.clicked.connect(self.onClick)
            self.listButton.append(button)

    def getNbrParameters(self, queryNbr):
        if queryNbr == 1 or queryNbr == 2 or queryNbr == 10:
            return 1
        elif queryNbr == 4 or queryNbr == 5:
            return 2
        elif queryNbr == 3 or queryNbr == 6 or queryNbr == 7 or queryNbr == 8 or queryNbr == 9:
            return 0



    def hideButton(self):
        for i in range(len(self.listButton)):
            self.listButton[i].hide()

    def showButton(self):
        for i in range(len(self.listButton)):
            self.listButton[i].show()

    def inputParameter(self):
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



    def doneClick(self):
        self.wait = True
        for i in range(len(self.listInputButton) - 1):
            self.listParameter.append(self.listInputButton[i].text())
            self.listInputButton[i].deleteLater()
        self.listInputButton[len(self.listInputButton) - 1].deleteLater()
        self.listInputButton.clear()
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
            label.move(200, 70+i*30)
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 700)
        self.pageWidget.append(button)
        self.showPage()

    def deletePage(self):
        for elem in self.pageWidget:
            elem.deleteLater()
        self.pageWidget.clear()

    def showPage(self):
        for elem in self.pageWidget:
            elem.show()

    def returnMenu(self):
        self.deletePage()
        self.showButton()

    def executeChange(self):
        "UPDATE your_table SET column1 = 'new_value' WHERE condition_column = 'condition_value'"
        toChange = self.pageWidget[1].currentText()
        newValue = self.pageWidget[0].text()
        if toChange == 'Pharmacien':
            cursor.execute("UPDATE ProjetDB.patient SET inami_pharmacien = %s WHERE NISS = %s", (newValue, self.NISS,))
        else:
            cursor.execute("UPDATE ProjetDB.patient SET inami_medecin = %s WHERE NISS = %s", (newValue, self.NISS,))
        self.cnx.commit()


    def modifyData(self):
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
        self.deletePage()
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 700)
        self.cursor.execute("SELECT date_diagnostic, pathology FROM ProjetDB.diagnostiques WHERE NISS = %s", (self.NISS,))
        label = QLabel("Vos diagnostiques", window)
        label.move(200, 100)
        self.pageWidget.append(label)
        i =0
        for elem in self.cursor:
            buff = 'Nom de la pathologie : ' + elem[1] + " et date de diagnostique " + str(elem[0])
            label = QLabel(buff, window)
            label.move(200, 150 + i * 20)
            self.pageWidget.append(label)
            i += 1
        self.pageWidget.append(button)
        self.showPage()

    def showTraitement(self):
        self.deletePage()
        button = QPushButton('Retour au menu', self)
        button.setToolTip('Envoyer les paramètres')
        button.clicked.connect(self.returnMenu)
        button.resize(200, 50)
        button.move(200, 700)
        self.pageWidget.append(button)
        self.cursor.execute("SELECT date_prescription, medicament_nom_commercial FROM ProjetDB.dossiers_patients WHERE NISS_patient = %s",
                            (self.NISS,))
        label = QLabel("Vos traitements :", window)
        label.move(200, 100)
        i = 0
        for elem in self.cursor:
            buff = 'Nom du médicament : ' + elem[1]+ " et date de prescription "+ str(elem[0])
            label = QLabel(buff, window)
            label.move(200, 150 + i * 20)
            self.pageWidget.append(label)
            i += 1
        print(i)
        self.pageWidget.append(label)
        self.showPage()


    def accountAction(self):
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
        NISSPatient = int(self.pageWidget[1].text())
        cursor.execute("SELECT * FROM ProjetDB.patient WHERE NISS = %s", (NISSPatient,))
        result = cursor.fetchone()
        if result:
            self.NISS = NISSPatient
            self.accountAction()


    def connection(self):
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
        if self.pageWidget[0].currentText() == "Patient":
            iter = 9
        elif self.pageWidget[0].currentText() == "Médecin":
            iter = 5
        else:
            iter = 4
        if len(self.pageWidget) != iter+4:
            if len(self.pageWidget) < iter+4:
                for i in range(len(self.pageWidget), iter+4):
                    inputBox = QLineEdit(self)
                    inputBox.resize(450,50)
                    inputBox.move(200, 70+(i-2)*70)
                    self.pageWidget.append(inputBox)
            elif len(self.pageWidget) > iter+4:
                for i in range(iter+4,len(self.pageWidget)):
                    self.pageWidget[i].deleteLater()
                    self.pageWidget.remove(self.pageWidget[i])
        self.showPage()


    def insertData(self):
        ValueToInsert = []
        for i in range(4, len(self.pageWidget)):
            ValueToInsert.append(self.pageWidget[i].text())
        if self.pageWidget[0].currentText() =="Patient":
            ValueToInsert[0] = int(ValueToInsert[0])
            ValueToInsert[2] = int(ValueToInsert[2])
            ValueToInsert[8] = int(ValueToInsert[8])
            ValueToInsert[3] = int(ValueToInsert[3])
            cursor.execute("INSERT INTO ProjetDB.patient (NISS, date_de_naissance, genre,inami_medecin, inami_pharmacien, mail, nom, prenon, telephone) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", ValueToInsert)
        elif self.pageWidget[0].currentText() =="Médecin":
            ValueToInsert[0] = int(ValueToInsert[0])
            ValueToInsert[4] = int(ValueToInsert[4])
            cursor.execute("INSERT INTO ProjetDB.medecins (inami, mail, nom, specialite,telephone) VALUES(%s,%s,%s,%s,%s)",ValueToInsert)
        else:
            ValueToInsert[0]= int(ValueToInsert[0])
            ValueToInsert[3] = int(ValueToInsert[3])
            cursor.execute("INSERT INTO ProjetDB.pharmacien (inami, mail, nom, telephone) VALUES(%s,%s,%s,%s)", ValueToInsert)
        cnx.commit()

    def addInfo(self):
        self.hideButton()
        label = QLabel("Choississez quelle information vous voulez ajouter :", window)
        label.move(150, 70)
        comboBox = QComboBox(self)
        comboBox.addItem("Patient")
        comboBox.addItem("Médecin")
        comboBox.addItem("Pharmacien")
        comboBox.move(200,150)
        comboBox.resize(200, 50)
        comboBox.currentIndexChanged.connect(self.selectionChanged)
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
        self.pageWidget.append(comboBox)
        self.pageWidget.append(sendButton)
        self.pageWidget.append(button)
        self.pageWidget.append(label)
        self.showPage()




    def onClick(self):
        sender = self.sender()
        self.position = int((sender.pos().y()-70)//70+1)
        self.nbrParameters = self.getNbrParameters(self.position)
        if self.position < 11:
            self.hideButton()
            self.inputParameter()
        else:
            if self.position == 11:
                self.addInfo()
            else:
                self.connection()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cnx = mysql.connector.connect(user='root', password='passpass',
                                  host='localhost',
                                  database='ProjetDB')
    cursor = cnx.cursor()
    window = MainWindow(cnx)
    window.show()
    sys.exit(app.exec_())