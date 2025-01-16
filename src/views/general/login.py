import sys

import bcrypt
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
from sql.db_connection import get_connection
from views.general.reception import ReceptionWindow
from views.general.registration import RegistrationWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Définir la taille de la fenêtre
        self.setGeometry(100, 100, 660, 385)
        self.setWindowTitle("Login Window")

        # Appliquer la couleur de fond
        self.setStyleSheet("background-color: #EFC8B1;")

        # Ajouter le label "Login"
        label = QtWidgets.QLabel("Login", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Centrer en haut
        label.setStyleSheet(
            "color: #514644; border-radius: 30px;"
        )  # Ajouter les bords arrondis au label

        # Définir la police du texte en gras et de taille 48
        font = QFont()
        font.setBold(True)
        font.setPointSize(48)
        label.setFont(font)

        # Positionner le label en haut
        label.move(275, 30)

        # Champ de texte "Username"
        self.username_field = QtWidgets.QLineEdit(self)
        self.username_field.setPlaceholderText("Username")  # Texte d'exemple
        self.username_field.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;  /* Bords arrondis de 17px */
            padding: 5px;
        """
        )
        self.username_field.setGeometry(
            220, 120, 220, 35
        )  # Centrer horizontalement et dimensionner le champ
        self.username_field.setAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )  # Aligner le texte à gauche

        # Appliquer une police en italique et taille 20
        font_username = QFont("Arial", 20)
        font_username.setItalic(True)
        self.username_field.setFont(font_username)

        # Champ de texte "Password"
        self.password_field = QtWidgets.QLineEdit(self)
        self.password_field.setPlaceholderText("Password")  # Texte d'exemple
        self.password_field.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;  /* Bords arrondis de 17px */
            padding: 5px;
        """
        )
        self.password_field.setGeometry(
            220, 190, 220, 35
        )  # Centrer horizontalement et dimensionner le champ
        self.password_field.setAlignment(
            Qt.AlignLeft | Qt.AlignVCenter
        )  # Aligner le texte à gauche

        # Appliquer une police en italique et taille 20
        font_password = QFont("Arial", 20)
        font_password.setItalic(True)
        self.password_field.setFont(font_password)

        # Activer le mode "Password" pour le champ mot de passe
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

        # Ajouter le bouton "Sign in"
        self.sign_in_button = QtWidgets.QPushButton("Sign in", self)
        self.sign_in_button.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;  /* Bords arrondis de 17px */
            padding: 5px;
            font-size: 20px;
            text-align: center;  /* Centrer le texte horizontalement */
        """
        )
        self.sign_in_button.setGeometry(
            240, 260, 181, 35
        )  # Positionner le bouton sous les champs texte et centré
        self.sign_in_button.setFont(QFont("Arial", 20))  # Police de taille 20

        # Ajouter un bouton "Registration request"
        self.registration_request_button = QtWidgets.QPushButton(
            "Registration request", self
        )
        self.registration_request_button.setStyleSheet(
            """
            background-color: transparent;
            color: #514644;
            border: none;
            font-size: 14px;
            text-align: center;
        """
        )
        self.registration_request_button.setGeometry(
            220, 310, 220, 35
        )  # Positionner le bouton sous "Sign in"
        self.registration_request_button.setFont(
            QFont("Arial", 14)
        )  # Police de taille 14

        # Connecter les boutons aux fonctions
        self.sign_in_button.clicked.connect(
            self.handle_login
        )  # Connecter le bouton "Sign in"
        self.registration_request_button.clicked.connect(
            self.open_registration_window
        )  # Connecter "Registration request"

        self.show()

    def handle_login(self):
        username = self.username_field.text()  # Correction
        password = self.password_field.text()  # Correction

        # Vérifie les données dans la base de données
        if self.verify_credentials(username, password):
            QMessageBox.information(self, "Succès", "Connexion réussie !")
            # Ici vous pouvez ouvrir la fenêtre de réception après une connexion réussie
            self.reception_window = ReceptionWindow()
            self.reception_window.show()
            self.close()  # Fermer la fenêtre de connexion
        else:
            QMessageBox.warning(
                self, "Erreur", "Nom d'utilisateur ou mot de passe incorrect."
            )

    def verify_credentials(self, username, password):
        connection = get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """
                SELECT Mot_de_passe_hash FROM Utilisateur WHERE Nom_utilisateur = %s
                """
                cursor.execute(query, (username,))
                result = cursor.fetchone()

                if result:
                    stored_hashed_password = result[0]
                    return bcrypt.checkpw(
                        password.encode("utf-8"), stored_hashed_password.encode("utf-8")
                    )
                return False
            except Exception as e:
                print(f"Erreur lors de la vérification des identifiants : {e}")
                return False
            finally:
                connection.close()
        return False

    def open_registration_window(self):
        self.registration_window = RegistrationWindow()
        self.registration_window.show()
        self.close()  # Fermer la fenêtre de connexion lorsque la fenêtre d'inscription est ouverte


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Créer l'application PyQt
    window = MainWindow()  # Créer la fenêtre principale
    window.show()  # Afficher la fenêtre principale
    sys.exit(app.exec_())  # Exécuter l'application
