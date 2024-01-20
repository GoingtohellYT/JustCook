from updateDB import check_user, set_current_user
import argon2
import sqlite3


class Request:

    def __init__(self, nom_db):
        # créer un pont avec la base de données pour pouvoir faire de requête SQL
        self.connexion = sqlite3.connect(nom_db)
        self.c = self.connexion.cursor()

    def give(self, table, nom):
        self.c.execute(f"SELECT {nom} FROM {table};")
        return self.c.fetchall()

    # fonction specifique
    def get_recettes(self, table, element, recette):
        """
        Fonction qui permet d'obtenir toutes les recettes d'une catégorie
        """
        self.c.execute(f"SELECT {element} FROM {table} WHERE categories LIKE '%{recette}%';")
        return self.c.fetchall()

    def get_recette_info(self, recette_id):
        """
        Fonction qui renvoie toutes les informations sur une recette
        """
        self.c.execute(f"SELECT * FROM recettes WHERE id = {recette_id}")
        return self.c.fetchall()[0]

    # fonction login(email, mdp)
    def login(self, email, mdp):
        if check_user(email):
            self.c.execute(f"SELECT mdp FROM users WHERE email LIKE '%{email}%';")
            mdp_hash = self.c.fetchall()[0][0]
            # print(mdp_hash)
            ph = argon2.PasswordHasher()
            if ph.verify(hash=mdp_hash, password=mdp):
                self.c.execute(f"SELECT dark_mode FROM user_settings WHERE email LIKE '%{email}%';")
                set_current_user(email)
                if self.c.fetchall()[0][0] == 0:
                    return True, False


request = Request('websiteDB.db')

# print(request.give('recettes', 'nom, image'))
# print(request.get_recette('recettes', 'nom', 'pâtes au beurre'))
# print(request.login('test.test@gmail.com', 'test'))
# print(request.get_recettes("recettes", "nom, id", "Pâtes"))
