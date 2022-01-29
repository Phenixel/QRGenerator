from cProfile import label
import qrcode
from qrcode import ERROR_CORRECT_M
from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import askcolor

window = Tk()
window.title("Qrgenerator")
window.geometry('800x500')

qr = qrcode.QRCode(
    version=5,
    error_correction=ERROR_CORRECT_M,
    box_size=3,
    border=5
)

##########################

def change_color():
    choseColor = askcolor(title="Choisir une couleur")[1]
    

def clicked():
    qr.add_data(link.get())
    qr.make(fit=True)

    img = qr.make_image(fill_color=choseColor.get(), back_color= backColor.get())
    img.save(nomFile.get()+'.png')
    messagebox.showinfo('Message title','Message content')

##########################

lblLink = Label(window, text="Entrez le lien vers lequel rediriger : ", font=("Arial Bold", 10))
lblLink.grid(column=0, row=0)

lblColor = Label(window, text="Entrez une couleur : ", font=("Arial Bold", 10))
lblColor.grid(column=0, row=1)

lblColorBack = Label(window, text="Entrez une couleur de fond : ", font=("Arial Bold", 10))
lblColorBack.grid(column=0, row=2)

lblNameFile = Label(window, text="Choisissez un nom pour votre fichier : ", font=("Arial Bold", 10))
lblNameFile.grid(column=0, row=3)

##########################

link = Entry(window,width=10)
link.grid(column=1, row=0)

choseColor = Entry(window,width=10)
choseColor.grid(column=2, row=1)

backColor = Entry(window,width=10)
backColor.grid(column=1, row=2)

nomFile = Entry(window,width=10)
nomFile.grid(column=1, row=3)

##########################

btn = Button(window, text="Générer", bg="white", fg="black", command=clicked)
btn.grid(column=0, row=5)

btn = Button(window, text="Select a Color", bg="white", fg="black", command=change_color)
btn.grid(column=1, row=1)

##########################
window.mainloop()