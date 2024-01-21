from tkinter import *
from tkinter import ttk
import requestDB


class RecipyPage:
    def __init__(self, recipy_id):
        self.id = recipy_id

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
        self.background_widgets.append(self.screen)

        self.screen.rowconfigure(0,weight=0)
        self.screen.rowconfigure(1,weight = 8)
        self.screen.rowconfigure(2,weight=1)

        self.screen.columnconfigure(0,weight=1)
        self.screen.columnconfigure(1,weight=6)
        self.screen.columnconfigure(2,weight=0)
        self.screen.columnconfigure(3,weight=0)

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

#________________Contenu principal de la fenêtre________________#

        self.side_panel = Frame(self.screen,background=self.main_color)
        self.main_widgets.append(self.side_panel)
        self.side_panel.grid(column=0,row=1,sticky=NSEW,rowspan=2)

        self.frame_scroll = Frame(self.screen)
        self.frame_scroll.grid(row=1, column=0, columnspan=4, sticky=NSEW)

        self.canvas = Canvas(self.frame_scroll,background=self.bg_color)
        self.canvas.pack(side=LEFT,fill=BOTH,expand=1)

        self.scrollbar = Scrollbar(self.frame_scroll,orient=VERTICAL,command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT,fill=Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>',lambda e:self.canvas.configure(scrollregion=self.canvas.bbox("all")))


        self.recette_frame = Frame(self.canvas,background=self.bg_color)
        self.background_widgets.append(self.recette_frame)
        self.recette_frame.pack(fill=BOTH,expand=1)
        self.recette_frame.columnconfigure(0,weight=0)

        self.canvas.create_window((0,0),window=self.recette_frame, anchor="nw")

        self.show_recipy()
       
#________________Le footer________________#
       
        self.btn_footer = Button(self.screen, text="Exit", bg=self.main_color, command=self.screen.destroy)
        self.main_widgets.append(self.btn_footer)
        self.btn_footer.grid(column=2, row=2, sticky=NSEW, columnspan=2)

        self.btn_night = Button(self.screen, text='Nightmode', command=self.screen_mode_update,background=self.main_color)
        self.main_widgets.append(self.btn_night)
        self.btn_night.grid(column=0, row=2, columnspan=2, sticky=NSEW)

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

    def get_recipy_infos(self):
        """
        Fonction qui permet de récupérer les informations d'une recette
        """
        infos = requestDB.request.get_recette_info(self.id)
        return infos
    
    def show_recipy(self):
        """
        Fonction qui affiche la recette
        """
        self.infos = self.get_recipy_infos()
        self.ingredients = self.infos[2].split(";")
        etapes = self.infos[3].split(";")
        
        self.titre_recette = Label(self.recette_frame,text=self.infos[1],font=("MV Boli",32),background=self.bg_color)
        self.background_widgets.append(self.titre_recette)
        self.titre_recette.pack(side=TOP,fill=BOTH,expand=1)
        
        self.image_rct = PhotoImage(file=self.infos[5])
        self.img_show = Label(self.recette_frame,image=self.image_rct,background=self.bg_color)
        self.background_widgets.append(self.img_show)
        self.img_show.pack(side=TOP,fill=BOTH,expand=1)

        for i in range(len(etapes)+len(self.ingredients)):
            if i==0:
                self.ing_titre = Label(self.recette_frame,text="Ingrédients:",font=("MV Boli",18),background=self.bg_color)
                self.background_widgets.append(self.ing_titre)
                self.ing_titre.pack(side=TOP,fill=BOTH,expand=1)
            elif i == len(self.ingredients):
                self.etp_titre = Label(self.recette_frame,text="Étapes:",font=("MV Boli",18),background=self.bg_color)
                self.background_widgets.append(self.etp_titre)
                self.etp_titre.pack(side=TOP,fill=BOTH,expand=1)
            if i < len(self.ingredients):
                self.recette_frame.rowconfigure(i,weight=0)
                self.ing = Label(self.recette_frame,text=self.ingredients[i],background=self.bg_color)
                self.background_widgets.append(self.ing)
                self.ing.pack(side=TOP,fill=BOTH,expand=1)
            elif i-len(self.ingredients) < len(etapes):
                self.recette_frame.rowconfigure(i,weight=0)
                self.etp = Label(self.recette_frame,text=etapes[i-len(self.ingredients)],background=self.bg_color)
                self.background_widgets.append(self.etp)
                self.etp.pack(side=TOP,fill=BOTH,expand=1)




#recipy = RecipyPage(0)
