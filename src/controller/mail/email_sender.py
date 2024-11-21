import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import keyring
from generate_password import pwd

# Fonction pour envoyer un e-mail
def send_email():
    service_name = "laposte"
    password = pwd(15)

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
    subject = "Test d'envoi avec laposte.net"
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
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")
    finally:
        server.quit()
        
send_email() # just for test