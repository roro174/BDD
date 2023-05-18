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
        super().__init__()
        self.parameters_ready = pyqtSignal(list)
        self.listQueries = ["La liste des noms commerciaux de médicaments correspondant à un nom en DCI, classés par ordre alphabétique et taille de conditionnement.",
                           "La liste des pathologies qui peuvent être prise en charge par un seul type de spécialistes.",
                            "La spécialité de médecins pour laquelle les médecins prescrivent le plus de médicaments.",
                            "Tous les utilisateurs ayant consommé un médicament spécifique (sous son nom commercial) aprés une date donnée, par exemple en cas de rappel de produit pour lot contaminé.",
                            "Tous les patients ayant été traités par un médicament (sous sa DCI) à une date antérieure mais qui ne le sont plus, pour vérifier qu’un patients suive bien un traitement chronique.",
                            "La liste des médecins ayant prescrit des médicaments ne relevant pas de leur spécialité.",
                            "Pour chaque décennie entre 1950 et 2020, (1950−59, 1960−69, ...), le médicament le plus consommé par des patients nés durant cette décennie.",
                            "Quelle est la pathologie la plus diagnostiquée ?",
                            "Pour chaque patient, le nombre de médecin lui ayant prescrit un médicament.",
                            "La liste de médicament n’étant plus prescrit depuis une date spécifique."]
        self.listButton = []
        self.listParameter = []
        self.listInput = []
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
            self.listInput.append(inputBox)
        button = QPushButton('ok', self)
        button.setToolTip('Envoyer les paramètres')
        button.move(200, 700)
        button.show()
        button.clicked.connect(self.doneClick)
        self.listInput.append(button)



    def doneClick(self):
        self.wait = True
        for i in range(len(self.listInput)-1):
            self.listParameter.append(self.listInput[i].text())
            self.listInput[i].deleteLater()
        self.listInput[len(self.listInput)-1].deleteLater()
        self.listInput.clear()
        query = Query(self.cnx, self.position, self.nbrParameters)
        self.drawAnswer(query.execute(self.listParameter))

    def drawAnswer(self, listAnswer):
        print(len(listAnswer))
        label = QLabel("Bonjour, PyQt5 !", window)
        label.move(200, 7)
        label.show()
        for i in range(len(listAnswer)):
            buf =''
            for j in range(len(listAnswer[i])):
                buf = buf + listAnswer[i][j] + ', '
            label = QLabel(buf, window)
            label.move(200, 70+i*70)
            label.show()

    def onClick(self):
        sender = self.sender()
        self.position = int((sender.pos().y()-70)//70+1)
        self.nbrParameters = self.getNbrParameters(self.position)
        self.hideButton()
        self.inputParameter()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    cnx = mysql.connector.connect(user='guest', password='passpass',
                                  host='localhost',
                                  database='Bdd')
    print(cnx.is_connected())
    window = MainWindow(cnx)
    window.show()
    sys.exit(app.exec_())