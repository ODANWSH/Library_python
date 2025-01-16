import mysql.connector
from mysql.connector import Error


def get_connection():
    """Retourne une connexion à la base de données."""
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="Bibliotheque"
        )
        return connection
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        return None
