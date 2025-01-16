import bcrypt

from sql.db_connection import get_connection


def hash_passwords():
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            # Récupérer tous les utilisateurs et leurs mots de passe
            query = "SELECT ID_Utilisateur, Mot_de_passe_hash FROM Utilisateur"
            cursor.execute(query)
            users = cursor.fetchall()

            for user in users:
                user_id, plain_password = user
                # Vérifiez si le mot de passe est déjà haché (facultatif)
                if not plain_password.startswith("$2b$"):
                    # Hachez le mot de passe
                    hashed_password = bcrypt.hashpw(
                        plain_password.encode("utf-8"), bcrypt.gensalt()
                    )
                    # Mettez à jour la base de données
                    update_query = "UPDATE Utilisateur SET Mot_de_passe_hash = %s WHERE ID_Utilisateur = %s"
                    cursor.execute(
                        update_query, (hashed_password.decode("utf-8"), user_id)
                    )

            connection.commit()
            print("Tous les mots de passe ont été hachés avec succès.")
        except Exception as e:
            print(f"Erreur lors du hachage des mots de passe : {e}")
        finally:
            connection.close()


# Exécuter la fonction
hash_passwords()
