from updateDB import check_user
import argon2
class Request:

    def __init__(self, nom_db):
        # créer un pont avec la base de donné pour pouvoir faire de requête sql
        self.connexion = sqlite3.connect(nom_db)
        self.c = self.connexion.cursor()

    def give(self, table, nom):
        self.c.execute(f"SELECT {nom} FROM {table} ;")
        return self.c.fetchall()

    #fonction specifique
    def get_recette(self, table, nom, recette):
        self.c.execute(f"SELECT {nom} FROM {table} WHERE {nom} LIKE '%{recette}%' ;")
        return self.c.fetchall()


    #fonction login(email, mdp)
    def login(self, email, mdp):
        if check_user(email) == True:
            self.c.execute(f"SELECT mdp FROM users WHERE email LIKE '%{email}%'")
            mdp_hash = self.c.fetchall()
            if argon2.PasswordHasher.verify(mdp_hash, mdp) == True:
                return True


request = Request('websiteDB.db')
print(request.give('recettes', 'nom, image'))
print(request.get_recette('recettes', 'nom', 'pâtes au beurre'))
print(request.login('test','test'))
