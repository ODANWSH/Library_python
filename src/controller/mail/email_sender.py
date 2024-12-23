import sqlite3
import bcrypt
from generate_password import pwd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import keyring

# Fonction pour insérer un mot de passe haché dans la base de données
def store_password(password_plain):
    # Connexion à la base de données SQLite (ou MySQL si vous préférez)
    conn = sqlite3.connect('user_database.db')  # Remplacez par votre connexion MySQL si nécessaire
    cursor = conn.cursor()

    # Créer une table si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Hachage du mot de passe
    password_hashed = bcrypt.hashpw(password_plain.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Insérer le mot de passe haché dans la base de données
    username = "user_example"  # Vous pouvez définir un nom d'utilisateur ici
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password_hashed))

    # Commit et fermeture de la connexion
    conn.commit()
    conn.close()

    print(f"Le mot de passe pour {username} a été enregistré avec succès dans la base de données.")

# Fonction pour envoyer un e-mail
def send_email():
    service_name = "laposte"
    password = pwd(15)  # Mot de passe en texte clair pour l'utilisateur

    # Récupération des identifiants
    sender_email = keyring.get_password(service_name, "email")
    if not sender_email:
        print("Erreur : aucune adresse e-mail trouvée. Configurez-la avec `store_credentials.py`.")
        return

    password_email = keyring.get_password(service_name, sender_email)
    if not password_email:
        print(f"Erreur : aucun mot de passe trouvé pour {sender_email}. Configurez-le avec `store_credentials.py`.")
        return

    receiver_email = "timeo.minarditm@gmail.com"
    subject = "Test"
    body = f"Bonjour,\n\nVoici vos identifiants :\n Name : Name\n Password :{password} \n Bonne lecture !"

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
        store_password(password)  # Enregistrer le mot de passe en base de données (haché)

    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")
    finally:
        server.quit()

# Appel de la fonction pour envoyer un e-mail
send_email()