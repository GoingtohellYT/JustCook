from tkinter import *
from tkinter import ttk
import sqlite3

import requestDB
import updateDB
import updateDB
import recipy_page
from requestDB import request


class Settings:
    def __init__(self, mode):
        self.day_sc_bg = "#a8bfe0"
        self.day_main = "#f7ee34"

        self.night_bg = "#634482"
        self.night_main = "#bca7d1"

        self.bg_color = self.day_sc_bg
        self.main_color = self.day_main

        self.is_night_mode = mode

        self.main_widgets = []
        self.background_widgets = []
        ##=================================================================##L'ECRAN##=================================================================##
        self.screen = Toplevel()
        self.screen.title("JustCook - settings")
        self.screen.geometry("1280x720")
        self.screen.resizable(0, 0)
        self.screen.configure(background=self.bg_color)

        self.screen.columnconfigure(0, weight=1)  # somehow, si on met les poids à 1 partout ils sont pas tous égaux
        self.screen.columnconfigure(1, weight=0)
        self.screen.columnconfigure(2, weight=3)
        self.screen.columnconfigure(3, weight=3)

        self.screen.rowconfigure(0, weight=0)
        self.screen.rowconfigure(1, weight=8)
        self.screen.rowconfigure(2, weight=0)

        self.background_widgets.append(self.screen)

        if self.is_night_mode:
            self.is_night_mode = False
            self.screen_mode_update()

        ##=================================================================##LES WIDGETS##=================================================================##

        # ________________Le header________________#

        self.header = Frame(self.screen, background=self.main_color)
        self.main_widgets.append(self.header)
        self.header.grid(row=0, column=0, columnspan=4)

        self.lbl_logo = ttk.Label(self.screen, text="JustCook")
        self.main_widgets.append(self.lbl_logo)
        self.lbl_logo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        self.lbl_logo.config(background=self.main_color, padding=(100, 0), font=("Z003", 45))

        # ---------------Le corps-----------------#
        self.corps = Frame(self.screen, background=self.bg_color)

        self.background_widgets.append(self.corps)

        self.corps.columnconfigure(0)
        self.corps.columnconfigure(1)

        self.corps.rowconfigure(0)
        self.corps.rowconfigure(1)
        self.corps.rowconfigure(2)

        # Bouton nightmode
        self.mode_pref = Label(self.corps, text="Nightmode par défaut")
        self.mode_pref.grid(row=0, column=0, padx=12)

        self.set_mode_pref = Button(self.corps, text="", command=lambda: self.toggle("mode"))
        self.set_mode_pref.grid(row=0, column=1, padx=12)

        # Bouton stay_logged_in
        self.stay_logged_pref = Label(self.corps, text="Rester connecté")
        self.stay_logged_pref.grid(row=1, column=0, padx=12)

        self.set_stay_logged = Button(self.corps, text="", command=lambda: self.toggle("stay_logged"))
        self.set_stay_logged.grid(row=1, column=1, padx=12)

        # Bouton déconnexion
        self.deconnect = Button(self.corps, text="Déconnexion", command=self.deconnect)
        self.deconnect.grid(row=2, column=0, pady=12)

        self.set_default_values()

        self.corps.grid(row=1, column=0)

        self.show_fav()

        # ________________Le footer________________#

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=2, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update,
                                background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=2, columnspan=2, sticky=NSEW)

        self.screen.mainloop()

    # _______________Les Fonctions_________________#
    def nightmode(self):
        if not self.is_night_mode:
            self.bg_color = self.night_bg
            self.main_color = self.night_main
            for e in self.main_widgets:
                e.configure(background=self.main_color)
            self.is_night_mode = True
            for e in self.background_widgets:
                e.configure(background=self.bg_color)
        else:
            self.bg_color = self.day_sc_bg
            self.main_color = self.day_main
            for e in self.main_widgets:
                e.configure(background=self.main_color)

            for e in self.background_widgets:
                e.configure(background=self.bg_color)
            self.is_night_mode = False
        self.screen.update()
        self.screen.update_idletasks()

    def screen_mode_update(self):
        Tk.after(self.screen, 500, self.nightmode)

    def set_default_values(self):
        """
        Fonction qui récupère les paramètres de l'utilisateur pour afficher les valeurs par défaut correspondantes
        """
        default_mode = request.get('dark_mode', "user_settings", "email", f'"{updateDB.current_user}"')[0][0]  # Pour le dark mode
        stay_logged = request.get('stay_logged_in', "user_settings", "email", f'"{updateDB.current_user}"')[0][0]  # Pour le stay logged in
        print(default_mode, stay_logged)

        if default_mode == 1:
            self.set_mode_pref.config(text="Oui")
        elif default_mode == 0:
            self.set_mode_pref.config(text="Non")

        if stay_logged == 1:
            self.set_stay_logged.config(text="Oui")
        elif stay_logged == 0:
            self.set_stay_logged.config(text="Non")

    def toggle(self, btn):
        """
        Fonction qui permet de changer le réglage par défaut
        """
        assert type(btn) is str and btn in ["mode", "stay_logged"]

        if btn == "mode":
            if self.set_mode_pref.config('text')[-1] == "Oui":
                updateDB.change_user_setting("dark_mode", 0)
                self.set_mode_pref.config(text="Non")
            elif self.set_mode_pref.config('text')[-1] == "Non":
                updateDB.change_user_setting("dark_mode", 1)
                self.set_mode_pref.config(text="Oui")
        else:
            if self.set_stay_logged.config('text')[-1] == "Oui":
                updateDB.change_user_setting("stay_logged_in", 0)
                self.set_stay_logged.config(text="Non")
            elif self.set_stay_logged.config('text')[-1] == "Non":
                updateDB.change_user_setting("stay_logged_in", 1)
                self.set_stay_logged.config(text="Oui")

    def deconnect(self):
        """
        Fonction qui déconnecte l'utilisateur
            - remet stay_logged_in sur False
            - met current_user à None
            - ferme la fenêtre des réglages utilisateurs
        """
        updateDB.change_user_setting("stay_logged_in", 0)
        updateDB.current_user = None
        print("logged out")
        self.screen.destroy()

    def get_fav(self, user):
        """
        Fonction qui permet de récupérer tous les id des recettes présents dans la table favoris et mis par l'utilisateur qui utilise l'app
        Prend en paramètre l'email de l'utilisateur connecté sous forme de string
        REnvoie une liste avec tous les id des recettes
        """
        return requestDB.request.get("id_recette", "favoris", "email", f'"{user}"')

    def show_fav(self):
        """
        Permet de faire afficher les recettes mise en favoris par 'utilisateur
        """
        try:
            fav = self.get_fav(updateDB.current_user)
            print(fav)

            for i in range(len(fav)):
                nom = requestDB.request.get_recette_info(fav[i][0])
                #add le nom de la recette avec le lien vers cette recette à l'affichage
                recette = Label(self.corps, text=f"Favoris n°{i+1} : {nom[1]}")
                recette.grid(column=0, row=i+3)
                btn_rectte = Button(self.corps, text='Accéder à la recette', command=lambda r_id=fav[i][0]: recipy_page.RecipyPage(r_id, self.is_night_mode), background=self.main_color)
                self.main_widgets.append(btn_rectte)
                btn_rectte.grid(column=1, row=i+3)

        except sqlite3.OperationalError:
            print("Cet utilisateur n'a pas encore de favoris")


