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
    WHERE id_recette LIKE {id_recette};
    """)

    result = c.fetchall()
    c.close()

    return email in result[0]


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

    connexion.commit()

    c.execute(f"""
    INSERT INTO user_settings
    VALUES ({0}, {0}, "{email}")
    """)

    connexion.commit()

    c.close()

    global current_user
    current_user = email


def add_recette(nom, ingredients, recette, categories, image, submitted_by):
    """
    Fonction qui ajoute une recette à la db

    Retourne :
        Rien
    Pré-conditions :
        tous les paramètres sont du type string (les ingredients sont séparés par des ';')
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
    # print(result)
    if result[0][0] is not None:  # S'il y a déjà des recettes dans la DB
        last_id = result[0][0]

        c.execute(f"""
        INSERT INTO recettes
        values (?, ?, ?, ?, ?, ?, ?);
        """, (last_id + 1, nom, ingredients, recette, categories, image, submitted_by))
    else:  # Si la table recettes est vide
        c.execute(f"""
        INSERT INTO recettes
        VALUES ({0}, "{nom}", "{ingredients}", "{recette}", "{categories}", "{image}", "{submitted_by}");
        """)

    connexion.commit()

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

        connexion.commit()

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

    connexion.commit()

    c.close()


# ------ Fonctions de modification de la DB ------ #
def change_user_setting(setting, value):
    """
    Fonction qui permet de changer un réglage utilisateur dans la DB

    Retourne :
        Rien
    Pré-conditions :
        setting est du type str et représente un réglage qui existe dans la DB
        value est du type int et varie entre 0 et 1 (False et True)
    """
    assert type(setting) is str and setting in ["dark_mode", "stay_logged_in"], "setting n'est pas une valeur acceptée"
    assert type(value) is int and (value == 0 or value == 1), "value n'a pas une valeur acceptée"

    global current_user

    connexion = sqlite3.connect("websiteDB.db")
    c = connexion.cursor()

    c.execute(f"""
    UPDATE user_settings
    SET "{setting}" = {value}
    WHERE email = "{current_user}";
    """)

    connexion.commit()
    c.close()


# ------ Tests ------ #
"""
add_user("test", "test", "test.test@gmail.com")
add_recette("Pâtes au beurre", "pâtes;eau;beurre", "faire bouillir de l'eau;mettre les pâtes;ajouter un peu de beurre quand le tout est cuit", "Pâtes", "./img_recettes/pates_au_beurre.jpg", "test.test@gmail.com")
add_recette("Pâtes à l'huile", "pâtes;eau;huile", "faire bouillir de l'eau;faire cuire les pâtes;ajouter un peu d'huile avant de servir", "Pâtes", "./img_recettes/pates_huile.jpg", "test.test@gmail.com")
add_user("Alex", "Alex", "alex.bonjour@gmail.com")
set_current_user("alex.bonjour@gmail.com")
add_comment(0, 4, "Classique mais ça fait toujours plaisir !")
add_favori(1)
"""


