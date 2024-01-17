from tkinter import *
from tkinter import ttk
from tkinter.font import Font

# from PIL import Image

# =============================================================================#Les Variables#=========================================================================================================#

day_sc_bg = "#a8bfe0"
day_main = "#f7ee34"

night_bg = "#634482"
night_main = "#bca7d1"

bg_color = day_sc_bg
main_color = day_main

is_night_mode = False

main_widgets = []
background_widgets = []


# =============================================================================#Les Variables#=========================================================================================================#


def nightmode():
    global is_night_mode
    global bg_color
    global main_color
    if not is_night_mode:
        bg_color = night_bg
        main_color = night_main
        for e in main_widgets:
            e.configure(background=main_color)
        is_night_mode = True
        for e in background_widgets:
            e.configure(background=bg_color)
    else:
        bg_color = day_sc_bg
        main_color = day_main
        for e in main_widgets:
            e.configure(background=main_color)

        for e in background_widgets:
            e.configure(background=bg_color)
        is_night_mode = False
    screen.update()
    screen.update_idletasks()
    # print(header.cget('background'))


def screen_mode_update():
    Tk.after(screen, 500, nightmode)


def test():
    print("duh")


# ===============================================================================#Le TKINTER#==========================================================================================================#
screen = Tk()
screen.title("JustCook")
screen.geometry("1280x720")
# screen.attributes('-fullscreen', True)  # met l'écren en fullscreen
screen.resizable(0, 0)
screen.configure(background=bg_color)

screen.rowconfigure(0, weight=0)
screen.rowconfigure(1, weight=4)
screen.rowconfigure(2, weight=0)
screen.rowconfigure(3, weight=5)
screen.rowconfigure(4, weight=0)
screen.rowconfigure(5, weight=0)

screen.columnconfigure(0, weight=1)  # somehow, si on met les poids à 1 partout ils sont pas tous égaux
screen.columnconfigure(1, weight=0)
screen.columnconfigure(2, weight=3)
screen.columnconfigure(3, weight=3)

background_widgets.append(screen)

header = Frame(screen, background=main_color)
main_widgets.append(header)
header.grid(row=0, column=0, columnspan=4)

lbl_logo = ttk.Label(screen, text="JustCook")
main_widgets.append(lbl_logo)
lbl_logo.grid(row=0, column=0, columnspan=4, sticky=NSEW)
lbl_logo.config(background=main_color, padding=(100, 0), font=("Z003", 45))

recette_cherchee = ""
barre_recherche = Entry(screen, textvariable=recette_cherchee, background="white")
barre_recherche.grid(row=0, column=2, columnspan=2, padx=250, sticky=EW)

img_user = PhotoImage(file="./images/user.png")
user = Button(screen, image=img_user, background='white')
user.grid(column=3, row=0)

img_entrees = PhotoImage(file="./images/entree.png")
entrees_lbl = Label(image=img_entrees)
entrees = Button(screen, image=img_entrees)
entrees.grid(column=0, row=1, pady=(15, 0), padx=30, sticky=NSEW)

btn_entrees = Button(screen, text="Entrées", bg=main_color)
main_widgets.append(btn_entrees)
btn_entrees.grid(column=0, row=2, sticky=NSEW, pady=(0, 5), padx=30)

img_pates = PhotoImage(file="./images/pates.png")
pates = Button(screen, image=img_pates).grid(column=1, row=1, sticky=NSEW, pady=(15, 0), padx=30)

btn_pates = Button(screen, text="Pâtes", bg=main_color)
main_widgets.append(btn_pates)
btn_pates.grid(column=1, row=2, sticky=NSEW, pady=(0, 5), padx=30)

img_viande = PhotoImage(file="./images/viande_modified.png")
viande = Button(screen, image=img_viande).grid(column=2, row=1, sticky=NSEW, pady=(15, 0), padx=30)

btn_viande = Button(screen, text="Viandes", bg=main_color)
main_widgets.append(btn_viande)
btn_viande.grid(column=2, row=2, sticky=NSEW, pady=(0, 5), padx=30)

img_poisson = PhotoImage(file="./images/poisson_modified.png")
poisson = Button(screen, image=img_poisson).grid(column=3, row=1, sticky=NSEW, pady=(15, 0), padx=30)

btn_poisson = Button(screen, text="Poissons", bg=main_color)
main_widgets.append(btn_poisson)
btn_poisson.grid(column=3, row=2, sticky=NSEW, pady=(0, 5), padx=30)

frm = Frame(screen, background=bg_color)  # Permet d'avoir 3 boutons sur la deuxième ligne sans que ça soit aligné avec ceux de la première ligne
background_widgets.append(frm)
frm.grid(row=4, column=0, columnspan=4, sticky=NSEW)

frm.columnconfigure(0, weight=1)
frm.columnconfigure(1, weight=1)
frm.columnconfigure(2, weight=1)

frm.rowconfigure(0, weight=3)
frm.rowconfigure(1, weight=1)

img_legumes = PhotoImage(file="./images/légumes.png")
legumes = Button(frm, image=img_legumes).grid(column=0, row=0, sticky=NSEW, pady=(5, 0), padx=30)

btn_legumes = Button(frm, text="Légumes", bg=main_color)
main_widgets.append(btn_legumes)
btn_legumes.grid(column=0, row=1, sticky=NSEW, pady=(0, 15), padx=30)

img_dessert = PhotoImage(file="./images/dessert.png")
dessert = Button(frm, image=img_dessert).grid(column=1, row=0, sticky=NSEW, pady=(5, 0), padx=30)

btn_desserts = Button(frm, text="Desserts", bg=main_color)
main_widgets.append(btn_desserts)
btn_desserts.grid(column=1, row=1, sticky=NSEW, pady=(0, 15), padx=30)

img_soupe = PhotoImage(file="./images/soupe.png")
soupe = Button(frm, image=img_soupe).grid(column=2, row=0, sticky=NSEW, pady=(5, 0), padx=30)

btn_soupe = Button(frm, text="Soupes", bg=main_color)
main_widgets.append(btn_soupe)
btn_soupe.grid(column=2, row=1, sticky=NSEW, pady=(0, 15), padx=30, columnspan=2)

btn_footer = Button(screen, text="Exit", bg=main_color, command=screen.destroy)
main_widgets.append(btn_footer)
btn_footer.grid(column=2, row=5, sticky=NSEW, columnspan=2)

btn_night = Button(screen, text='Nightmode', command=screen_mode_update, background=main_color)
main_widgets.append(btn_night)
btn_night.grid(column=0, row=5, columnspan=2, sticky=NSEW)

screen.mainloop()
