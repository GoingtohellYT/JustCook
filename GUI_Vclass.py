from tkinter import *
from tkinter import ttk
import requestDB
from PIL import Image,ImageTk
from tkinter.font import Font
import recipy_page

# import updateDB

# from PIL import Image


# =============================================================================#Les Variables#=========================================================================================================#
class Homepage:

    def __init__(self):

        self.day_sc_bg = "#a8bfe0"
        self.day_main = "#f7ee34"

        self.night_bg = "#634482"
        self.night_main = "#bca7d1"

        self.bg_color = self.day_sc_bg
        self.main_color = self.day_main

        self.is_night_mode = False

        self.main_widgets = []
        self.background_widgets = []

##=================================================================##L'ECRAN##=================================================================##

        self.screen = Tk()
        self.screen.title("JustCook")
        self.screen.geometry("1280x720")
        # screen.attributes('-fullscreen', True)  # met l'écren en fullscreen
        self.screen.resizable(0, 0)
        self.screen.configure(background=self.bg_color)

        self.screen.rowconfigure(0, weight=0)
        self.screen.rowconfigure(1, weight=4)
        self.screen.rowconfigure(2, weight=0)
        self.screen.rowconfigure(3, weight=5)
        self.screen.rowconfigure(4, weight=0)
        self.screen.rowconfigure(5, weight=0)

        self.screen.columnconfigure(0, weight=1)  # somehow, si on met les poids à 1 partout ils sont pas tous égaux
        self.screen.columnconfigure(1, weight=0)
        self.screen.columnconfigure(2, weight=3)
        self.screen.columnconfigure(3, weight=3)

        self.background_widgets.append(self.screen)

##=================================================================##LES WIDGETS##=================================================================##

#________________Le header________________#

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

        self.img_user = PhotoImage(file="./images/user.png")
        self.user = Button(self.screen, image=self.img_user, background='white', command=self.login)
        self.user.grid(column=3, row=0)

#________________Contenu principal de la fenêtre________________#

        self.img_entrees = PhotoImage(file="./images/entree.png")
        self.entrees_lbl = Label(image=self.img_entrees)
        self.entrees = Button(self.screen, image=self.img_entrees, command=self.see_entrees)
        self.entrees.grid(column=0, row=1, pady=(15, 0), padx=30, sticky=NSEW)

        self.btn_entrees = Button(self.screen, text="Entrées", bg=self.main_color, command=self.see_entrees)
        self.main_widgets.append(self.btn_entrees)
        self.btn_entrees.grid(column=0, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_pates = PhotoImage(file="./images/pates.png")
        self.pates = Button(self.screen, image=self.img_pates, command=self.see_pates).grid(column=1, row=1, sticky=NSEW, pady=(15, 0), padx=30)

        self.btn_pates = Button(self.screen, text="Pâtes", bg=self.main_color, command=self.see_pates)
        self.main_widgets.append(self.btn_pates)
        self.btn_pates.grid(column=1, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_viande = PhotoImage(file="./images/viande_modified.png")
        viande = Button(self.screen, image=self.img_viande, command=self.see_viandes).grid(column=2, row=1, sticky=NSEW, pady=(15, 0), padx=30)

        self.btn_viande = Button(self.screen, text="Viandes", bg=self.main_color, command=self.see_viandes)
        self.main_widgets.append(self.btn_viande)
        self.btn_viande.grid(column=2, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_poisson = PhotoImage(file="./images/poisson_modified.png")
        self.poisson = Button(self.screen, image=self.img_poisson, command=self.see_poissons).grid(column=3, row=1, sticky=NSEW, pady=(15, 0), padx=30)

        self.btn_poisson = Button(self.screen, text="Poissons", bg=self.main_color, command=self.see_poissons)
        self.main_widgets.append(self.btn_poisson)
        self.btn_poisson.grid(column=3, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.frm = Frame(self.screen, background=self.bg_color)  # Permet d'avoir 3 boutons sur la deuxième ligne sans que ça soit aligné avec ceux de la première ligne
        self.background_widgets.append(self.frm)
        self.frm.grid(row=4, column=0, columnspan=4, sticky=NSEW)

        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        self.frm.columnconfigure(2, weight=1)

        self.frm.rowconfigure(0, weight=3)
        self.frm.rowconfigure(1, weight=1)

        self.img_legumes = PhotoImage(file="./images/légumes.png")
        self.legumes = Button(self.frm, image=self.img_legumes, command=self.see_legumes).grid(column=0, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_legumes = Button(self.frm, text="Légumes", bg=self.main_color, command=self.see_legumes)
        self.main_widgets.append(self.btn_legumes)
        self.btn_legumes.grid(column=0, row=1, sticky=NSEW, pady=(0, 15), padx=30)

        self.img_dessert = PhotoImage(file="./images/dessert.png")
        self.dessert = Button(self.frm, image=self.img_dessert, command=self.see_desserts).grid(column=1, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_desserts = Button(self.frm, text="Desserts", bg=self.main_color, command=self.see_desserts)
        self.main_widgets.append(self.btn_desserts)
        self.btn_desserts.grid(column=1, row=1, sticky=NSEW, pady=(0, 15), padx=30)

        self.img_soupe = PhotoImage(file="images/soupe.png")
        self.soupe = Button(self.frm, image=self.img_soupe, command=self.see_soupes).grid(column=2, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_soupe = Button(self.frm, text="Soupes", bg=self.main_color, command=self.see_soupes)
        self.main_widgets.append(self.btn_soupe)
        self.btn_soupe.grid(column=2, row=1, sticky=NSEW, pady=(0, 15), padx=30, columnspan=2)

#________________Le footer________________#

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=5, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update,background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=5, columnspan=2, sticky=NSEW)

        self.screen.mainloop()

##=================================================================##LES FONCTIONS##=================================================================##


    def nightmode(self):

        if not self.is_night_mode:
            self.bg_color = self.night_bg
            self.main_color = self.night_main
            for e in self.main_widgets:
                e.configure(background=self.main_color)
            self.is_night_mode = True
            for e in self.background_widgets:
                e.configure(background=self.bg_color)
            self.btn_night.configure(text="Light mode")
        else:
            self.bg_color = self.day_sc_bg
            self.main_color = self.day_main
            for e in self.main_widgets:
                e.configure(background=self.main_color)

            for e in self.background_widgets:
                e.configure(background=self.bg_color)
                self.btn_night.configure(text="Night mode")
            self.is_night_mode = False

        self.screen.update()
        self.screen.update_idletasks()
        # print(header.cget('background'))

    def screen_mode_update(self):
        Tk.after(self.screen, 500, self.nightmode)

    def login(self):
        self.screen.destroy()
        loginpage = Login()

    def see_entrees(self):
        self.screen.destroy()
        CategoryPage("Entrée")

    def see_pates(self):
        self.screen.destroy()
        CategoryPage("Pâtes")

    def see_viandes(self):
        CategoryPage("Viandes")

    def see_poissons(self):
        self.screen.destroy()
        CategoryPage("Soupes")

    def see_legumes(self):
        self.screen.destroy()
        CategoryPage("Légumes")

    def see_desserts(self):
        self.screen.destroy()
        CategoryPage("Desserts")

    def see_soupes(self):
        self.screen.destroy()
        CategoryPage("Soupes")

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("240x100")
        self.root.title('Login')
        self.root.resizable(0, 0)

        # configure the grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)

        # username
        self.username_label = ttk.Label(self.root, text="Email:")
        self.username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

        self.username_entry = ttk.Entry(self.root)
        self.username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

        # password
        self.password_label = ttk.Label(self.root, text="Password:")
        self.password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

        # login button
        self.login_button = ttk.Button(self.root, text="Login", command=self.log)
        self.login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)

        self.root.mainloop()

    def log(self):
        """
        Fonction qui permet de récupérer l'email et le mot de passe entré par l'utilisateur et de le connecter
        """
        email = self.username_entry.get()
        pwd = self.password_entry.get()

        login_try = requestDB.request.login(email, pwd)

        if login_try[0]:
            print("logged in")
            if login_try[1]:
                test.nightmode()
                print("switch to nightmode")

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
        ##=================================================================##L'ECRAN##=================================================================##
        self.screen = Tk()
        self.screen.title("JustCook")
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

        ##=================================================================##LES WIDGETS##=================================================================##

        # ________________Le header________________#

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

        # ________________Contenu principal de la fenêtre________________#

        self.recette_frame = Frame(self.screen, background=self.bg_color)
        self.background_widgets.append(self.recette_frame)
        self.recette_frame.grid(row=1, column=0, columnspan=4, sticky=NSEW)
        self.recette_frame.columnconfigure(0, weight=1)  # somehow, si on met les poids à 1 partout ils sont pas tous égaux
        self.recette_frame.columnconfigure(1, weight=1)
        self.recette_frame.columnconfigure(2, weight=1)
        self.recette_frame.columnconfigure(3, weight=1)

        # ________________Le footer________________#

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=5, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update,
                                background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=5, columnspan=2, sticky=NSEW)

        self.create_rows()

        self.screen.mainloop()

    ##=================================================================##LES FONCTIONS##=================================================================##

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
        recettes = requestDB.request.get_recettes("recettes", "nom, id, image",self.category)  # appel la fonction de Matteo
        print(recettes)
        nb_lignes = len(recettes) / 4  # on affiche 4 recettes

        if len(recettes) != 0:
            if int(nb_lignes) != float(nb_lignes):
                nb_lignes = int(nb_lignes)
                nb_lignes += 1
            else:
                nb_lignes = int(nb_lignes)

            # print(nb_lignes)

            index = 0
            images = list()
            btns = list()
            indexes = list()

            for i in range(nb_lignes):
                self.recette_frame.rowconfigure(i)
                for j in range(4):
                    if index < len(recettes):
                        print(index)
                        image_recette = Image.open(recettes[index][2])
                        image_recette = ImageTk.PhotoImage(image_recette.resize((250, 250)))
                        setattr(CategoryPage, "image_recette_"+str(index), image_recette)
                        images.append(getattr(CategoryPage, "image_recette_"+str(index)))
                        # print(self.image_recette)
                        btns.append((ttk.Button(self.recette_frame, text=recettes[index][0],
                                                       image=images[index], compound=TOP,
                                                       command=lambda m=recettes[index][1]: self.go_to_selected_recipy(m))))
                        indexes.append((i, j))
                        #self.image_bouton.grid(row=i, column=j)
                        index += 1

            for i in range(len(btns)):
                btns[i].grid(row=indexes[i][0], column=indexes[i][1])

    def go_to_selected_recipy(self, recette_id):
        """
        Fonction qui permet d'afficher la page de la recette choisie par l'utilisateur
        """
        self.screen.destroy()
        recipy_page.RecipyPage(recette_id)



# ===============================================================================#Le TKINTER#==========================================================================================================#
test = Homepage()
