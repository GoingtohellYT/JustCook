from tkinter import *
from tkinter import ttk
import updateDB
import updateDB
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

        self.mode_pref = Label(self.corps, text="Nightmode par défaut")
        self.mode_pref.grid(row=0, column=0, padx=12)

        self.set_mode_pref = Button(self.corps, text="", command=lambda: self.toggle("mode"))
        self.set_mode_pref.grid(row=0, column=1, padx=12)

        self.set_default_values()

        self.corps.grid(row=1, column=0)

        # ________________Le footer________________#

        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=2, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update,
                                background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=2, columnspan=2, sticky=NSEW)

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

    def set_default_values(self):
        """
        Fonction qui récupère les paramètres de l'utilisateur pour afficher les valeurs par défaut correspondantes
        """
        default_mode = request.get('dark_mode', "user_settings", "email", f'"{updateDB.current_user}"')[0][0]  # Pour le dark mode
        if default_mode == 1:
            self.set_mode_pref.config(text="Oui")
        elif default_mode == 0:
            self.set_mode_pref.config(text="Non")

    def toggle(self, btn):
        """
        Fonction qui permet de changer le réglage par défaut
        """
        if btn == "mode":
            if self.set_mode_pref.config('text')[-1] == "Oui":
                updateDB.change_user_setting("dark_mode", 0)
                self.set_mode_pref.config(text="Non")
            elif self.set_mode_pref.config('text')[-1] == "Non":
                updateDB.change_user_setting("dark_mode", 1)
                self.set_mode_pref.config(text="Oui")
