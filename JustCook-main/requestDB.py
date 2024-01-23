from updateDB import check_user, set_current_user
import argon2
import sqlite3


class Request:

    def __init__(self, nom_db):
        # créer un pont avec la base de données pour pouvoir faire de requête SQL
        self.connexion = sqlite3.connect(nom_db)
        self.c = self.connexion.cursor()

    def give(self, table, nom):
        """
        Fonction qui permet de faire des requêtes sql à une base de donnée quelconque.
        Prend en paramètre :
            -Le nom de la table
            -Un ou des attributs de la table
        Renvoie :
            -Une liste avec les données demandées
        """
        self.c.execute(f"SELECT {nom} FROM {table};")
        return self.c.fetchall()

    # fonction spécifique
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

    def get(self, attribut, table, condition1=None, condition2= None):
        """
        Fonction qui permet d'accéder à la base de données en fonction d'une condition qui dépend de l'attribut
        """
        if condition1 == None:
            self.c.execute(f"SELECT {attribut} FROM {table}")
        else:
            self.c.execute(f"SELECT {attribut} FROM {table} WHERE {condition1} = {condition2}")
        return self.c.fetchall()

    # fonction login(email, mdp)
    def login(self, email, mdp):
        """
        La fonction permet de vérifier si un utilisateur à rentrer le bon email et le bon mot de passe.
        Prend en paramètre :
            - email : email rentré par l'utilisateur
            - mdp : mot de passe rentré par l'utilisateur
        Renvoie :
            - un boolen : Vrai si tout correspond False sinon
        """
        if check_user(email):
            self.c.execute(f"SELECT mdp FROM users WHERE email LIKE '%{email}%';")
            mdp_hash = self.c.fetchall()[0][0]
            # print(mdp_hash)
            ph = argon2.PasswordHasher()
            if ph.verify(hash=mdp_hash, password=mdp):
                self.c.execute(f"SELECT dark_mode FROM user_settings WHERE email LIKE '%{email}%';")
                set_current_user(email)
                darkmode = self.c.fetchall()[0][0]
                print(darkmode)
                if darkmode == 0:
                    return True, False
                elif darkmode == 1:
                    return True, True
            else:
                return False, False


request = Request('websiteDB.db')

# print(request.give('recettes', 'nom, image'))
# print(request.get_recette('recettes', 'nom', 'pâtes au beurre'))
# print(request.login('test.test@gmail.com', 'test'))
# print(request.get_recettes("recettes", "nom, id", "Pâtes"))
