from tkinter import *
from tkinter import ttk
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

        self.screen.rowconfigure(0,weight=0)
        self.screen.rowconfigure(1,weight=8)
        self.screen.rowconfigure(2,weight=0)

        self.header = Frame(self.screen, background=self.main_color)
        self.main_widgets.append(self.header)
        self.header.grid(row=0, column=0, columnspan=4)

        self.lbl_logo = ttk.Label(self.screen, text="JustCook")
        self.main_widgets.append(self.lbl_logo)
        self.lbl_logo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        self.lbl_logo.config(background=self.main_color, padding=(100, 0), font=("Z003", 45))

        self.recette_cherchee = ""
        self.barre_recherche = Entry(self.screen, textvariable=self.recette_cherchee, background="white")
        self.barre_recherche.grid(row=0, column=2, columnspan=2, padx=250, sticky=EW)


        self.recette_frame = Frame(self.screen,background="red")
        self.background_widgets.append(self.recette_frame)
        self.recette_frame.grid(row=1,column=0,columnspan=4,sticky=NSEW)
        self.recette_frame.columnconfigure(0, weight=1)  # somehow, si on met les poids à 1 partout ils sont pas tous égaux
        self.recette_frame.columnconfigure(1, weight=1)
        self.recette_frame.columnconfigure(2, weight=1)
        self.recette_frame.columnconfigure(3, weight=1)

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=5, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update,background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=5, columnspan=2, sticky=NSEW)

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
        recettes = requestDB.request.get_recettes("recettes", "nom, id, image", self.category)  # appel la fonction de Matteo
        print(recettes)
        nb_lignes = len(recettes) / 4  # on affiche 4 recettes

        if len(recettes) != 0:
            if int(nb_lignes) != float(nb_lignes):
                nb_lignes = int(nb_lignes)
                nb_lignes += 1

            print(nb_lignes)

            for i in range(nb_lignes):
                self.recette_frame.rowconfigure(i)
                for j in range(4):
                    if 2*i+j < len(recettes):
                        image_recette = PhotoImage(file=recettes[2*i+j][2])
                        #image_bouton = Button(self.recette_frame,image=image_recette)
                        #image_bouton.grid(column=j,row=i+1)
                        recette = Button(self.recette_frame, text=recettes[2*i+j][0],image = image_recette,compound=TOP, command=lambda m=recettes[2*i+j][1]: self.go_to_selected_recipy(m))
                        recette.grid(column=j, row=i+1,pady=15)

    def go_to_selected_recipy(self, recette_id):
        """
        Fonction qui permet d'afficher la page de la recette choisie par l'utilisateur
        """
        recipy_page.RecipyPage(recette_id)