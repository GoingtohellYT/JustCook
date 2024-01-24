from tkinter import *
from tkinter import ttk
import os
import requestDB
import cat_page
from settings import Settings
import updateDB
from requestDB import request


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

        if os.name == "nt":
            self.titlesfont = ("MV Boli",18)
            self.logofont = ("MV Boli",45)
        elif os.name == "posix":
            self.titlesfont = ("Z003",18)
            self.logofont = ("Z003",45)
        else:
            self.titlesfont = ("Times New Roman",18)
            self.logofont = ("Times New Roman",45)
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

        # ________________Le header________________#

        self.header = Frame(self.screen, background=self.main_color)
        self.main_widgets.append(self.header)
        self.header.grid(row=0, column=0, columnspan=4)

        self.lbl_logo = ttk.Label(self.screen, text="JustCook")
        self.main_widgets.append(self.lbl_logo)
        self.lbl_logo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        self.lbl_logo.config(background=self.main_color, padding=(100, 0), font=self.logofont)

        self.img_user = PhotoImage(file="./images/user.png")
        self.user = Button(self.screen, image=self.img_user, background='white', command=self.login)
        self.user.grid(column=3, row=0)

        self.img_add = PhotoImage(file="./images/add.png")
        self.add = Button(self.screen, image=self.img_add, background="red", command=self.add_recette)
        self.add.grid(column=2, row=0)

        # ________________Contenu principal de la fenêtre________________#

        self.img_entrees = PhotoImage(file="./images/entree.png")
        self.entrees_lbl = Label(image=self.img_entrees)
        self.entrees = Button(self.screen, image=self.img_entrees, command=self.see_entrees)
        self.entrees.grid(column=0, row=1, pady=(15, 0), padx=30, sticky=NSEW)

        self.btn_entrees = Button(self.screen, text="Entrées", bg=self.main_color, font=self.titlesfont, command=self.see_entrees)
        self.main_widgets.append(self.btn_entrees)
        self.btn_entrees.grid(column=0, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_pates = PhotoImage(file="./images/pates.png")
        self.pates = Button(self.screen, image=self.img_pates, command=self.see_pates).grid(column=1, row=1,sticky=NSEW, pady=(15, 0),padx=30)

        self.btn_pates = Button(self.screen, text="Pâtes", bg=self.main_color, font=self.titlesfont, command=self.see_pates)
        self.main_widgets.append(self.btn_pates)
        self.btn_pates.grid(column=1, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_viande = PhotoImage(file="./images/viande_modified.png")
        self.viande = Button(self.screen, image=self.img_viande, command=self.see_viandes).grid(column=2, row=1, sticky=NSEW,pady=(15, 0), padx=30)

        self.btn_viande = Button(self.screen, text="Viandes", bg=self.main_color, font=self.titlesfont, command=self.see_viandes)
        self.main_widgets.append(self.btn_viande)
        self.btn_viande.grid(column=2, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_poisson = PhotoImage(file="./images/poisson_modified.png")
        self.poisson = Button(self.screen, image=self.img_poisson, command=self.see_poissons).grid(column=3, row=1,sticky=NSEW,pady=(15, 0),padx=30)

        self.btn_poisson = Button(self.screen, text="Poissons", bg=self.main_color, font=self.titlesfont, command=self.see_poissons)
        self.main_widgets.append(self.btn_poisson)
        self.btn_poisson.grid(column=3, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.frm = Frame(self.screen,background=self.bg_color)  # Permet d'avoir 3 boutons sur la deuxième ligne sans que ça soit aligné avec ceux de la première ligne
        self.background_widgets.append(self.frm)
        self.frm.grid(row=4, column=0, columnspan=4, sticky=NSEW)

        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        self.frm.columnconfigure(2, weight=1)

        self.frm.rowconfigure(0, weight=3)
        self.frm.rowconfigure(1, weight=1)

        self.img_legumes = PhotoImage(file="./images/légumes.png")
        self.legumes = Button(self.frm, image=self.img_legumes, command=self.see_legumes).grid(column=0, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_legumes = Button(self.frm, text="Légumes", bg=self.main_color, font=self.titlesfont, command=self.see_legumes)
        self.main_widgets.append(self.btn_legumes)
        self.btn_legumes.grid(column=0, row=1, sticky=NSEW, pady=(0, 15), padx=30)

        self.img_dessert = PhotoImage(file="./images/dessert.png")
        self.dessert = Button(self.frm, image=self.img_dessert, command=self.see_desserts).grid(column=1, row=0,sticky=NSEW,pady=(5, 0), padx=30)

        self.btn_desserts = Button(self.frm, text="Desserts", bg=self.main_color, font=self.titlesfont, command=self.see_desserts)
        self.main_widgets.append(self.btn_desserts)
        self.btn_desserts.grid(column=1, row=1, sticky=NSEW, pady=(0, 15), padx=30)

        self.img_soupe = PhotoImage(file="images/soupe.png")
        self.soupe = Button(self.frm, image=self.img_soupe, command=self.see_soupes).grid(column=2, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_soupe = Button(self.frm, text="Soupes", bg=self.main_color, font=self.titlesfont, command=self.see_soupes)
        self.main_widgets.append(self.btn_soupe)
        self.btn_soupe.grid(column=2, row=1, sticky=NSEW, pady=(0, 15), padx=30, columnspan=2)

        # ________________Le footer________________#

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, font=self.titlesfont, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=5, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', font=self.titlesfont, command=self.screen_mode_update,
                                background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=5, columnspan=2, sticky=NSEW)

        self.check_auto_login()  # On vérifie la connexion auto d'un user

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
        if updateDB.current_user is None:
            Login(self)
        else:
            Settings(self.is_night_mode)
    def add_recette(self):
        if updateDB.current_user is not None:
            Add_recette(self, updateDB.current_user)
    def check_auto_login(self):
        """
        Fonction qui permet de vérifier si un utilisateur a la connexion automatique activée
        et de le connecter si c'est le cas
        """
        try:
            potential_user = request.get("email", "user_settings", "stay_logged_in", 1)[0][0]
            if updateDB.check_user(potential_user):
                updateDB.set_current_user(potential_user)
                print("Connexion automatique !")
                if request.get("dark_mode", "user_settings", "email", f'"{potential_user}"')[0][0] == 1:
                    self.screen_mode_update()  # On active le nightmode si c'est dans ses préférences
        except IndexError:
            print("Aucun utilisateur n'a la connexion automatique d'activée")

    def see_entrees(self):
        cat_page.CategoryPage("Entrée", self.is_night_mode)

    def see_pates(self):
        cat_page.CategoryPage("Pâtes", self.is_night_mode)

    def see_viandes(self):
        cat_page.CategoryPage("Viandes", self.is_night_mode)

    def see_poissons(self):
        cat_page.CategoryPage("Poissons", self.is_night_mode)

    def see_legumes(self):
        cat_page.CategoryPage("Légumes", self.is_night_mode)

    def see_desserts(self):
        cat_page.CategoryPage("Desserts", self.is_night_mode)

    def see_soupes(self):
        cat_page.CategoryPage("Soupes", self.is_night_mode)


class Login:
    def __init__(self, homepage):
        self.homepage = homepage

        self.root = Toplevel()
        self.root.geometry("240x100")
        self.root.title('Login')
        self.root.resizable(0,0)

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
            updateDB.set_current_user(email)
            print("logged in")
            if login_try[1]:
                self.homepage.screen_mode_update()
                print("switch to nightmode")
        self.root.destroy()

class Add_recette:

    def __init__(self, homepage, account):

        self.homepage = homepage
        self.account = account

        self.screen = Toplevel()
        self.screen.geometry("500x500")
        self.screen.title('Ajouter une recette')
        self.screen.resizable(0,0)
        self.screen.configure(background=self.homepage.bg_color)

        self.screen.columnconfigure(0, weight=1)
        self.screen.columnconfigure(1, weight=10)

        self.header = Frame(self.screen, background=self.homepage.main_color)

        self.header.grid(row=0, column=0, columnspan=4)

        self.lbl_logo = ttk.Label(self.screen, text="JustCook")
        self.lbl_logo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        self.lbl_logo.config(background=self.homepage.main_color, padding=(100, 0), font=self.homepage.logofont)


        # nom
        self.name_label = ttk.Label(self.screen, text="Nom:",background=self.homepage.bg_color)
        self.name_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

        self.name_entry = ttk.Entry(self.screen)
        self.name_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

        # ingredients
        self.ingredients_label = ttk.Label(self.screen, text="Ingredients:",background=self.homepage.bg_color)
        self.ingredients_label.grid(column=0, row=2, sticky=W, padx=5, pady=5)

        self.ingredients_entry = ttk.Entry(self.screen)
        self.ingredients_entry.grid(column=1, row=2, sticky=E, padx=5, pady=5)

        #recette
        self.recette_label = ttk.Label(self.screen, text="Recette:",background=self.homepage.bg_color)
        self.recette_label.grid(column=0, row=3, sticky=W, padx=5, pady=5)

        self.recette_entry = ttk.Entry(self.screen)
        self.recette_entry.grid(column=1, row=3, sticky=E, padx=5, pady=5)

        #categorie
        self.categorie_label = ttk.Label(self.screen, text="Categorie:",background=self.homepage.bg_color)
        self.categorie_label.grid(column=0, row=4, sticky=W, padx=5, pady=5)

        self.categorie_entry = ttk.Entry(self.screen,background=self.homepage.bg_color)
        self.categorie_entry.grid(column=1, row=4, sticky=E, padx=5, pady=5)

        #image
        self.image_label = ttk.Label(self.screen, text="Path:",background=self.homepage.bg_color)
        self.image_label.grid(column=0, row=5, sticky=W, padx=5, pady=5)

        self.image_entry = ttk.Entry(self.screen)
        self.image_entry.grid(column=1, row=5, sticky=E, padx=5, pady=5)

        # Add button
        self.add_button = Button(self.screen, text="ADD", command=self.add,background=self.homepage.main_color)
        self.add_button.grid(column=1, row=6, sticky=E, padx=5, pady=5)

        self.screen.mainloop()

    def add(self):
        """
        Fonction qui permet de récupérer l'email et le mot de passe entré par l'utilisateur et de le connecter
        """
        nom = self.name_entry.get()
        ingredients = self.ingredients_entry.get()
        recette = self.recette_entry.get()
        categories = self.categorie_entry.get()
        image= self.image_entry.get()
        submitted_by = self.account


        login_try = updateDB.add_recette(nom,ingredients,recette,  categories, image, submitted_by)
        self.screen.destroy()

def popupmsg(msg):
    popup = Toplevel()

    popup.geometry("200x150")
    popup.title('ATTENTION /!\ ')
    popup.resizable()

    w = 200  # width for the Tk root
    h = 150  # height for the Tk root

    # get screen width and height
    ws = popup.winfo_screenwidth()  # width of the screen
    hs = popup.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    popup.geometry('%dx%d+%d+%d' % (w, h, x, y))

    popup.columnconfigure(0, weight=1)
    popup.columnconfigure(1, weight=1)
    popup.columnconfigure(2, weight=1)

    label = Label(popup, text=msg)
    label.grid(column=1, row=0, pady=w//4)

    B1 = Button(popup, text="Okay", command=popup.destroy)
    B1.grid(column=1, row=1)
    popup.mainloop()
# ===============================================================================#Le TKINTER#==========================================================================================================#
homepage = Homepage()
