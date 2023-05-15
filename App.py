import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QWidget, \
    QComboBox, QFileDialog, QGroupBox, QGridLayout
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QColor, QPainter, QBrush, QPalette



class App(QWidget):
    "classe qui contient toutes les informations de la fenêtre"
    def __init__(self):
        super().__init__()
        #self.listQueries = ["req1", "resq2"]
        self.title = "Info-H303 : Base de données"
        self.left = 5
        self.top = 40
        self.width = 1950
        self.height = 980
    
    """def createButton(self):
        for i in range(self.listQueries.len()):
            button = QPushButton(self.listQueries[i], self)
            button.setToolTip('Choisir cette requête')
            button.move(100,70+i*70)
            button.clicked.connect(self.on_click)"""
    


def main():
    app = QApplication(sys.argv)
    ex = App()
    ex.exec_()
    sys.exit(app.exec_())


if __name__ == "__main__":  
    main()