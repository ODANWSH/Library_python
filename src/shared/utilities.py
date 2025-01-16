import bcrypt
from sql.db_connection import get_connection


def store_password(username: str, email: str, password_plain: str):
    # Connexion à la base de données
    conn = (
        get_connection()
    )  # Assurez-vous que get_connection retourne une instance valide
    cursor = conn.cursor()

    # Hachage du mot de passe
    password_hashed = bcrypt.hashpw(
        password_plain.encode("utf-8"), bcrypt.gensalt()
    ).decode("utf-8")

    # Insérer le mot de passe haché dans la base de données
    cursor.execute(
        """
        INSERT INTO Utilisateur (Nom_Utilisateur, Mot_de_passe_hash, Email)
        VALUES (%s, %s, %s)
        """,
        (username, password_hashed, email),
    )

    conn.commit()
    conn.close()

    print(f"Mot de passe pour {username} enregistré avec succès.")


import smtplib
import keyring
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from shared.utilities import (
    store_password,
)  # Assurez-vous que cette fonction est bien importée


def send_email(email: str, password: str):
    service_name = "laposte"

    # Récupération des identifiants
    sender_email = keyring.get_password(service_name, "email")
    if not sender_email:
        print(
            "Erreur : aucune adresse e-mail trouvée. Configurez-la avec `store_credentials.py`."
        )
        return

    password_email = keyring.get_password(service_name, sender_email)
    if not password_email:
        print(
            f"Erreur : aucun mot de passe trouvé pour {sender_email}. Configurez-le avec `store_credentials.py`."
        )
        return

    receiver_email = email  # Utilisation de l'email fourni en paramètre
    subject = "Test"
    body = f"Bonjour,\n\nVoici vos identifiants :\n Name : Name\n Password : {password} \nBonne lecture !"

    # Création du message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        # Connexion au serveur SMTP
        server = smtplib.SMTP_SSL("smtp.laposte.net", 465)
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("E-mail envoyé avec succès !")

        # Enregistrer le mot de passe en base de données après l'envoi du mail
        store_password(
            "Nom d'utilisateur", email, password
        )  # Exemple d'appel à store_password

    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")
    finally:
        server.quit()
