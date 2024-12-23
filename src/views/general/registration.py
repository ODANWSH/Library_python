from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
import sys


class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Définir la taille de la fenêtre
        self.setGeometry(100, 100, 660, 385)
        self.setWindowTitle("Registration Window")

        # Appliquer la couleur de fond
        self.setStyleSheet("background-color: #EFC8B1;")

        # Layout principal vertical
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(0, 10, 0, 0)  # Réduction des marges pour maximiser l'espace vertical

        # Ajouter le label "Registration"
        label = QtWidgets.QLabel(
            "You don’t have the permission to register. "
            "Please enter your name and your email. An administrator "
            "will create your account and send your connection ID.",
            self,
        )
        label.setAlignment(Qt.AlignCenter)  # Centrer horizontalement
        label.setWordWrap(True)  # Permet le retour à la ligne automatique
        label.setStyleSheet("""
            color: #514644;
            background-color: transparent;
            padding: 10px;
        """)  # Couleur du texte et ajout de padding pour l'esthétique

        # Définir la police du texte
        font = QFont()
        font.setBold(True)
        font.setPointSize(16)
        label.setFont(font)

        main_layout.addWidget(label)  # Ajouter le label en haut

        # Ajouter un espace après le label (30 pixels)
        main_layout.addSpacing(30)

        # Champ de texte "Name"
        self.name_field = QtWidgets.QLineEdit(self)
        self.name_field.setPlaceholderText("Name")  # Texte d'exemple
        self.name_field.setStyleSheet("""
            background-color: #514644;
            color: white;
            border-radius: 17px;
            padding: 5px;
        """)
        self.name_field.setFixedSize(220, 35)  # Taille fixe
        main_layout.addWidget(self.name_field, alignment=Qt.AlignHCenter)

        # Champ de texte "First Name"
        self.first_name_field = QtWidgets.QLineEdit(self)
        self.first_name_field.setPlaceholderText("First Name")  # Texte d'exemple
        self.first_name_field.setStyleSheet("""
            background-color: #514644;
            color: white;
            border-radius: 17px;
            padding: 5px;
        """)
        self.first_name_field.setFixedSize(220, 35)  # Taille fixe
        main_layout.addWidget(self.first_name_field, alignment=Qt.AlignHCenter)

        # Champ de texte "Email"
        self.email_field = QtWidgets.QLineEdit(self)
        self.email_field.setPlaceholderText("Email")
        self.email_field.setStyleSheet("""
            background-color: #514644;
            color: white;
            border-radius: 17px;
            padding: 5px;
        """)
        self.email_field.setFixedSize(220, 35)
        main_layout.addWidget(self.email_field, alignment=Qt.AlignHCenter)

        # Ajouter le bouton "Send Request"
        self.send_request_button = QtWidgets.QPushButton("Send Request", self)
        self.send_request_button.setStyleSheet("""
            background-color: #514644;
            color: white;
            border-radius: 17px;
            padding: 5px;
            font-size: 20px;
        """)
        self.send_request_button.setFixedSize(181, 35)

        # Ajouter un espace de 20 pixels entre le dernier champ texte et le bouton
        main_layout.addSpacing(20)
        main_layout.addWidget(self.send_request_button, alignment=Qt.AlignHCenter)

        # Ajouter une flèche en haut à gauche pour revenir à la fenêtre de connexion
        self.back_button = QtWidgets.QPushButton(self)
        self.back_button.setGeometry(20, 20, 50, 50)  # Positionner la flèche en haut à gauche
        self.back_button.setStyleSheet("background-color: transparent; border: none;")

        # Vérifier si le chemin de l'icône est valide
        icon_path = "../assets/icons8-flèche-gauche-100.png"  # Assurez-vous du chemin
        if not QtGui.QIcon(icon_path).isNull():
            back_icon = QtGui.QIcon(icon_path)
            self.back_button.setIcon(back_icon)
            self.back_button.setIconSize(QSize(40, 40))
        else:
            print(f"Icon not found at: {icon_path}. Using default text.")
            self.back_button.setText("←")  # Utiliser un texte si l'icône est introuvable

        # Connecter le bouton à la fonction pour revenir à la fenêtre de connexion
        self.back_button.clicked.connect(self.back_to_login)

        self.show()

    def back_to_login(self):
        # Importer MainWindow ici pour éviter l'import circulaire
        from login import MainWindow
        # Retourner à la fenêtre de connexion
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()  # Fermer la fenêtre d'inscription


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = RegistrationWindow()
    sys.exit(app.exec_())