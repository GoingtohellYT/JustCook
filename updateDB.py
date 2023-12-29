import sqlite3
import argon2

current_user = None


# ------ Fonctions de vérification dans la DB ------ #
def check_user(email):
    """
    Fonction qui vérifie si l'utilisateur existe

    Retourne :
        True ou False selon si l'utilisateur est dans la DB
    Pré-conditions :
        email est un email valide
    Post-conditions :
        un booléen est renvoyé et la DB n'est pas modifiée
    """
    assert "@" in email and "." in email, "l'email n'est pas valide"

    connexion = sqlite3.connect('websiteDB.db')
    c = connexion.cursor()

    c.execute(f"""
    SELECT email FROM users
    WHERE email LIKE "{email}";
    """)

    result = c.fetchall()
    c.close()
    return len(result) == 1


def set_current_user(email):
    """
    Sets the current user to the specified email
    """
    assert check_user(email), "L'utilisateur n'existe pas"

    global current_user
    current_user = email


def check_recette(id_recette):
    """
    Fonction qui vérifie si la recette est présente dans la DB

    Retourne :
        True ou False selon si la recette est dans la DB
    Pré-conditions :
        id_recette est un integer supérieur ou égal à 0
    Post-conditions :
        Un booléen est renvoyé et la DB n'est pas modifiée
    """
    assert type(id_recette) is int and id_recette >= 0

    connexion = sqlite3.connect('websiteDB.db')
    c = connexion.cursor()

    c.execute(f"""
    SELECT id FROM recettes
    WHERE id LIKE {id_recette};
    """)

    result = c.fetchall()
    c.close()
    return len(result) == 1


def check_favoris(email, id_recette):
    """
    Fonction qui vérifie si une recette fait partie des favoris d'un utilisateur

    Retourne :
        True ou False selon si la recette fait partie des favoris de l'utilisateur
    Pré-conditions :
        id_recette est l'identifiant d'une recette existante
        email est l'email d'un utilisateur existant
    Post-conditions :
        Un booléen est renvoyé et la DB n'est pas modifiée
    """
    assert check_recette(id_recette), "La recette n'existe pas"
    assert check_user(email), "L'utilisateur n'existe pas"

    connexion = sqlite3.connect("websiteDB.db")
    c = connexion.cursor()

    c.execute(f"""
    SELECT email FROM favoris
    WHERE id_recette LIKE ?;
    """, (id_recette))

    result = c.fetchall()
    c.close()

    return email in result


# ------ Fonctions d'ajout dans la DB ------ #
def add_user(pseudo, mdp, email):
    """
    Fonction qui permet d'ajouter un utilisateur à la db

    Retourne :
        Rien
    Pré-conditions :
        pseudo est du type string
        mdp est du type string
        email est du type string
    Post-conditions :
        un nouvel utilisateur est ajouté à la db
    """
    assert type(pseudo) is str, "pseudo is not str"
    assert type(mdp) is str, "mdp is not str"
    assert type(email) is str, "email is not str"
    assert "@" in email and "." in email, "email not valid"

    ph = argon2.PasswordHasher()
    hashed_mdp = ph.hash(mdp)
    print(hashed_mdp)
    connexion = sqlite3.connect('websiteDB.db')
    c = connexion.cursor()

    c.execute(f"""
    INSERT INTO users
    VALUES ("{pseudo}", "{str(hashed_mdp)}", "{email}");
    """)

    c.close()

    global current_user
    current_user = email


def add_recette(nom, ingredients, categories, submitted_by):
    """
    Fonction qui ajoute une recette à la db

    Retourne :
        Rien
    Pré-conditions :
        tous les paramètres sont du type string (les ingredients sont séparés par des ';'
    """
    assert type(nom) is str
    assert type(ingredients) is str
    assert type(categories) is str
    assert check_user(submitted_by)

    connexion = sqlite3.connect('websiteDB.db')
    c = connexion.cursor()

    c.execute("""
    SELECT MAX(id) FROM recettes;
    """)

    result = c.fetchall()
    print(result)
    if result[0][0] is not None:  # S'il y a déjà des recettes dans la DB
        last_id = result[0][0]

        c.execute(f"""
        INSERT INTO recettes
        values (?, ?, ?, ?, ?);
        """, (last_id + 1, nom, ingredients, categories, submitted_by))
    else:  # Si la table recettes est vide
        c.execute(f"""
        INSERT INTO recettes
        VALUES ({0}, "{nom}", "{ingredients}", "{categories}", "{submitted_by}");
        """)
    c.close()


def add_favori(id_recette):
    """
    Fonction qui ajoute un favori à l'utilisateur actuel

    Retourne :
        Rien
    Pré-conditions :
        id_recette est un integer qui correspond à l'id d'une recette dans la table recettes
    Post-conditions :
        La recette est ajoutée à l'utilisateur actuel
    """
    assert type(id_recette) is int

    if check_recette(id_recette):
        global current_user

        connexion = sqlite3.connect('websiteDB.db')
        c = connexion.cursor()

        request = f"""
        INSERT INTO favoris
        values ("{current_user}", {id_recette});
        """

        print(request)

        c.execute(request)

        c.close()


def add_comment(recette_id, note, comment):
    """
    Fonction qui permet d'ajouter un commentaire à la table comments

    Retourne :
        Rien
    Pré-conditions :
        recette_id est l'id d'une recette dans la DB
        note est un integer compris entre 0 et 5
        comment est une string qui contient le commentaire
    Post-conditions :
        un commentaire est ajouté à la table comments
    """
    assert check_recette(recette_id), "recette inconnue"
    assert type(note) is int and 0 <= note <= 5, "note impossible"
    assert type(comment) is str, "Mauvais format de commentaire"

    global current_user

    connexion = sqlite3.connect('websiteDB.db')
    c = connexion.cursor()

    c.execute(f"""
    INSERT INTO comments
    values (?, ?, ?, ?);
    """, (current_user, recette_id, note, comment))

    c.close()

# ------ Fonctions de modification de la DB ------ #


# ------ Tests ------ #

# add_user("Alexis", "my_great_pwd", "alexis.mengual@orange.fr")
# add_recette("pâtes au beurre", "pâtes;beurre", "plat de résistance", "alexis.mengual@orange.fr")
# add_favori(0)
# add_comment(0, 3, "basique mais fait le taf")


