from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QSpacerItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from shared.utilities import send_email, store_password

class RegistrationWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Définir la taille de la fenêtre
        self.setGeometry(100, 100, 660, 385)
        self.setWindowTitle("Registration Window")

        # Appliquer la couleur de fond
        self.setStyleSheet("background-color: #EFC8B1;")

        # Ajouter le label "Registration"
        label = QLabel("Registration", self)
        label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)  # Centrer en haut
        label.setStyleSheet(
            "color: #514644; border-radius: 30px;"  # Ajouter les bords arrondis au label
        )

        # Définir la police du texte en gras et de taille 48
        font = QFont()
        font.setBold(True)
        font.setPointSize(48)
        label.setFont(font)

        # Positionner le label en haut
        label.move(220, 30)

        # Layout principal
        main_layout = QVBoxLayout()

        # Ajouter un espacement extensible avant les champs de texte
        main_layout.addStretch(1)

        # Champ "Name"
        self.name_field = QLineEdit(self)
        self.name_field.setPlaceholderText("Name")
        self.name_field.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;  /* Bords arrondis de 17px */
            padding: 5px;
            font-style: italic;
            text-align: left;
        """
        )
        self.name_field.setAlignment(Qt.AlignLeft)  # Aligner le texte à gauche
        self.name_field.setFont(QFont("Arial", 18))  # Réduit la taille de la police
        self.name_field.setFixedSize(220, 35)  # Taille définie à 220x35px
        main_layout.addWidget(self.name_field)

        # Champ "First Name"
        self.first_name_field = QLineEdit(self)
        self.first_name_field.setPlaceholderText("First name")
        self.first_name_field.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;  /* Bords arrondis de 17px */
            padding: 5px;
            font-style: italic;
            text-align: left;
        """
        )
        self.first_name_field.setAlignment(Qt.AlignLeft)  # Aligner le texte à gauche
        self.first_name_field.setFont(QFont("Arial", 18))  # Réduit la taille de la police
        self.first_name_field.setFixedSize(220, 35)  # Taille définie à 220x35px
        main_layout.addWidget(self.first_name_field)

        # Champ "Email"
        self.email_field = QLineEdit(self)
        self.email_field.setPlaceholderText("Email")
        self.email_field.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;
            padding: 5px;
            font-style: italic;
            text-align: left;
        """
        )
        self.email_field.setAlignment(Qt.AlignLeft)  # Aligner le texte à gauche
        self.email_field.setFont(QFont("Arial", 18))  # Réduit la taille de la police
        self.email_field.setFixedSize(220, 35)  # Taille définie à 220x35px
        main_layout.addWidget(self.email_field)

        # Ajouter un espacement de 20px avant le bouton
        main_layout.addSpacing(20)

        # Bouton "Send Request"
        self.send_request_button = QPushButton("Send Request")
        self.send_request_button.setStyleSheet(
            """
            background-color: #514644;
            color: white;
            border-radius: 17px;  /* Bords arrondis */
            padding: 5px;
            font-size: 20px;
        """
        )
        self.send_request_button.setFont(QFont("Arial", 20))
        self.send_request_button.setFixedSize(180, 35)  # Taille définie à 180x35px
        main_layout.addWidget(self.send_request_button)

        # Ajouter un espacement extensible après le bouton
        main_layout.addStretch(1)

        # Connecter le bouton à la méthode handle_request
        self.send_request_button.clicked.connect(self.handle_request)

        self.setLayout(main_layout)

    def handle_request(self):
        # Récupérer les valeurs des champs
        username = self.name_field.text()
        email = self.email_field.text()
        password = self.password_field.text()

        if username and email and password:
            # Stocker le mot de passe
            store_password(username, email, password)

            # Envoyer l'email
            send_email(email, password)
        else:
            print("Veuillez remplir tous les champs.")