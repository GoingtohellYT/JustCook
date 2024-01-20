from tkinter import *
import requestDB
import recipy_page


# from requestDB import ...


class CategoryPage:
    def __init__(self, category):
        self.category = category

        self.day_sc_bg = "#a8bfe0"
        self.day_main = "#f7ee34"

        self.night_bg = "#634482"
        self.night_main = "#bca7d1"

        self.bg_color = self.day_sc_bg
        self.main_color = self.day_main

        self.is_night_mode = False

        self.main_widgets = []
        self.background_widgets = []

        self.screen = Tk()
        self.screen.title("JustCook")
        self.screen.geometry("1280x720")
        self.screen.resizable(0, 0)
        self.screen.configure(background=self.bg_color)

        self.screen.columnconfigure(0, weight=1)  # somehow, si on met les poids à 1 partout ils sont pas tous égaux
        self.screen.columnconfigure(1, weight=0)
        self.screen.columnconfigure(2, weight=3)
        self.screen.columnconfigure(3, weight=3)

        self.create_rows()

        self.screen.mainloop()

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

    def create_rows(self):
        """
        Fonction qui crée le bon nombre de lignes selon le nombre de recettes et crée un bouton au bon
        emplacement par recette
        """
        recettes = requestDB.request.get_recettes("recettes", "nom, id", self.category)  # appel la fonction de Matteo
        print(recettes)
        nb_lignes = len(recettes) / 4  # on affiche 4 recettes

        if len(recettes) != 0:
            if int(nb_lignes) != float(nb_lignes):
                nb_lignes = int(nb_lignes)
                nb_lignes += 1

            print(nb_lignes)

            for i in range(nb_lignes):
                self.screen.rowconfigure(i)
                for j in range(4):
                    if 2*i+j < len(recettes):
                        recette = Button(self.screen, text=recettes[2*i+j][0], command=lambda m=recettes[2*i+j][1]: self.go_to_selected_recipy(m))
                        recette.grid(column=j, row=i)

    def go_to_selected_recipy(self, recette_id):
        """
        Fonction qui permet d'afficher la page de la recette choisie par l'utilisateur
        """
        recipy_page.RecipyPage(recette_id)
