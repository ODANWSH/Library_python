from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class ReceptionWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent, flags)

        # Définir la taille de la fenêtre
        self.setGeometry(100, 100, 660, 385)
        self.setWindowTitle("Accueil Window")

        # Appliquer la couleur de fond
        self.setStyleSheet("background-color: #EFC8B1;")
