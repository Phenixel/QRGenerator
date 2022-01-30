from cProfile import label
import qrcode
from qrcode import ERROR_CORRECT_M
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor

# Mise en place de la fenêtre

window = Tk()
window.title("Qrgenerator")
window.geometry('795x500')
bg = PhotoImage(file = "assets/fond.png")
window.iconbitmap('assets/icone.ico')

# parametre du qrcode

qr = qrcode.QRCode(
    version=5,
    error_correction=ERROR_CORRECT_M,
    box_size=3,
    border=5
)

############# Functions #############

def change_color():
    global choseColor
    choseColor = askcolor(title="Choisir une couleur")[1]

def change_color_back():
    global backColor
    backColor = askcolor(title="Choisir une couleur de fond")[1]

def generate():
    if link.get() != "":
        #  AND choseColor != "" AND back_color != ""
        qr.add_data(link.get())
        qr.make(fit=True)
        img = qr.make_image(fill_color=choseColor, back_color= backColor)
        img.save(nomFile.get()+'.png')
        messagebox.showinfo('Oppération réussie','Votre qr code a bien été généré !')
    else:
        messagebox.showwarning('Champs manquant','Un ou plusieurs champs sont manquants. Merci de bien vouloir les remplir.')

############# Labels #############

lblForBack = Label( window, image = bg)
lblForBack.place(x = -5, y = 0)

lblLink = Label(window, text="Entrez le lien vers lequel rediriger : ", font=("Arial Bold", 15), bg = "#ffdaef")
lblLink.grid(column=0, row=0, padx=70, pady=(170, 10))

lblColor = Label(window, text="Entrez une couleur : ", font=("Arial Bold", 15), bg = "#ffdaef")
lblColor.grid(column=0, row=1, padx=70, pady=10)

lblColorBack = Label(window, text="Entrez une couleur de fond : ", font=("Arial Bold", 15), bg = "#ffdaef")
lblColorBack.grid(column=0, row=2, padx=70, pady=10)

lblNameFile = Label(window, text="Choisissez un nom pour votre fichier : ", font=("Arial Bold", 15), bg = "#ffdaef")
lblNameFile.grid(column=0, row=3, padx=70, pady=10)

############# Entry #############

link = Entry(window,width=40)
link.grid(column=1, row=0, pady=(170, 10))

nomFile = Entry(window,width=40)
nomFile.grid(column=1, row=3)

############# Button #############

btn = Button(window, text="Générer", bg="white", fg="black", command=generate)
btn.grid(column=0, row=5)

btn = Button(window, text="Select a Color", bg="white", fg="black", command=change_color)
btn.grid(column=1, row=1)

btn = Button(window, text="Select a Color", bg="white", fg="black", command=change_color_back)
btn.grid(column=1, row=2)

############# Fin #############
window.mainloop()