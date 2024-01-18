from tkinter import *
from tkinter import ttk
from tkinter.font import Font
#import updateDB

# from PIL import Image

# =============================================================================#Les Variables#=========================================================================================================#


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


        self.screen = Tk()
        self.screen.title("JustCook")
        self.screen.geometry("1280x720")
        #screen.attributes('-fullscreen', True)  # met l'écren en fullscreen
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

        self.img_entrees = PhotoImage(file="./images/entree.png")
        self.entrees_lbl = Label(image=self.img_entrees)
        self.entrees = Button(self.screen, image=self.img_entrees)
        self.entrees.grid(column=0, row=1, pady=(15, 0), padx=30, sticky=NSEW)

        self.btn_entrees = Button(self.screen, text="Entrées", bg=self.main_color)
        self.main_widgets.append(self.btn_entrees)
        self.btn_entrees.grid(column=0, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_pates = PhotoImage(file="./images/pates.png")
        self.pates = Button(self.screen, image=self.img_pates).grid(column=1, row=1, sticky=NSEW, pady=(15, 0), padx=30)

        self.btn_pates = Button(self.screen, text="Pâtes", bg=self.main_color)
        self.main_widgets.append(self.btn_pates)
        self.btn_pates.grid(column=1, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_viande = PhotoImage(file="./images/viande_modified.png")
        viande = Button(self.screen, image=self.img_viande).grid(column=2, row=1, sticky=NSEW, pady=(15, 0), padx=30)

        self.btn_viande = Button(self.screen, text="Viandes", bg=self.main_color)
        self.main_widgets.append(self.btn_viande)
        self.btn_viande.grid(column=2, row=2, sticky=NSEW, pady=(0, 5), padx=30)

        self.img_poisson = PhotoImage(file="./images/poisson_modified.png")
        self.poisson = Button(self.screen, image=self.img_poisson).grid(column=3, row=1, sticky=NSEW, pady=(15, 0), padx=30)

        self.btn_poisson = Button(self.screen, text="Poissons", bg=self.main_color)
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
        self.legumes = Button(self.frm, image=self.img_legumes).grid(column=0, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_legumes = Button(self.frm, text="Légumes", bg=self.main_color)
        self.main_widgets.append(self.btn_legumes)
        self.btn_legumes.grid(column=0, row=1, sticky=NSEW, pady=(0, 15), padx=30)

        self.img_dessert = PhotoImage(file="./images/dessert.png")
        self.dessert = Button(self.frm, image=self.img_dessert).grid(column=1, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_desserts = Button(self.frm, text="Desserts", bg=self.main_color)
        self.main_widgets.append(self.btn_desserts)
        self.btn_desserts.grid(column=1, row=1, sticky=NSEW, pady=(0, 15), padx=30)

        self.img_soupe = PhotoImage(file="./images/soupe.png")
        self.soupe = Button(self.frm, image=self.img_soupe).grid(column=2, row=0, sticky=NSEW, pady=(5, 0), padx=30)

        self.btn_soupe = Button(self.frm, text="Soupes", bg=self.main_color)
        self.main_widgets.append(self.btn_soupe)
        self.btn_soupe.grid(column=2, row=1, sticky=NSEW, pady=(0, 15), padx=30, columnspan=2)

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=5, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update, background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=5, columnspan=2, sticky=NSEW)

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


    def test():
        print("duh")

    def login(self):
        loginpage = Login()

class Login:
    def __init__(self):
        root = Tk()
        root.geometry("240x100")
        root.title('Login')
        root.resizable(0, 0)

        # configure the grid
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)


        # username
        username_label = ttk.Label(root, text="Username:")
        username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

        username_entry = ttk.Entry(root)
        username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

        # password
        password_label = ttk.Label(root, text="Password:")
        password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

        password_entry = ttk.Entry(root,  show="*")
        password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(root, text="Login")
        login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)


        root.mainloop()

# ===============================================================================#Le TKINTER#==========================================================================================================#
test = Homepage()