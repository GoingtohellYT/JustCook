import sqlite3

connexion = sqlite3.connect('websiteDB.db')

c = connexion.cursor()

# -- Création des tables --
c.execute("""
    CREATE TABLE IF NOT EXISTS users(
    pseudo TEXT,
    mdp TEXT,
    email TEXT PRIMARY KEY);
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS user_settings(
    dark_mode INT,
    stay_logged_in INT,
    email TEXT PRIMARY KEY,
    FOREIGN KEY (email) REFERENCES users (email));
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS recettes(
    id INTEGER PRIMARY KEY,
    nom TEXT,
    ingredients TEXT,
    recette TEXT,
    categories TEXT,
    image TEXT,
    submitted_by TEXT,
    FOREIGN KEY (submitted_by) REFERENCES users (email));
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS favoris(
    email TEXT,
    id_recette INTEGER,
    PRIMARY KEY (email, id_recette),
    FOREIGN KEY (email) REFERENCES users (email),
    FOREIGN KEY (id_recette) REFERENCES recettes (id));
""")

c.execute("""
    CREATE TABLE IF NOT EXISTS comments(
    user_email TEXT,
    recette_id INTEGER,
    note FLOAT,
    comment TEXT,
    PRIMARY KEY (user_email, recette_id),
    FOREIGN KEY (user_email) REFERENCES users (email),
    FOREIGN KEY (recette_id) REFERENCES recettes (id));
""")
