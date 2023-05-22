from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QWidget, \
    QComboBox, QFileDialog, QGroupBox, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt, QRect, pyqtSignal
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush, QPalette


class Query:
    def __init__(self, cnx, queryType, nbrParameter):
        self.cnx = cnx
        self.queryType = queryType
        self.nbrParameter = nbrParameter

    def splitRequet(self, requet):
        splitreq = requet.split(";")
        for elem in splitreq:
            elem = elem + ";"
        return splitreq

    def execute(self, parametre):
        cursor = self.cnx.cursor()
        match self.queryType:
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
                if(self.queryType == "insérer"):
                    query = ("SELECT nom, prenom FROM table")
                    cursor.execute(query)
                elif(self.queryType == "se connecter"):
                    query = ("SELECT nom, prenom FROM table")
                    cursor.execute(query)
                return
        for i in range(self.nbrParameter):
            replaceValue = '$' + str(i+1)
            script = script.replace(replaceValue, parametre[i])
        splitreq = self.splitRequet(script)
        for req in splitreq:
            cursor.execute(req)
        retValue = []
        for x in cursor:
            retValue.append(x)

        return retValue

