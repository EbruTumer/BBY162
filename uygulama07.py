from tkinter import *
from PIL import Image, ImageTk
album = Tk()
album.title("Limni Gölü Fotoğraf Albümü")


fotoğraf1 = ImageTk.PhotoImage(Image.open("fotoğraf1.jpg"))
fotoğraf2 = ImageTk.PhotoImage(Image.open("fotoğraf2.jpg"))

etiket = Label(album, text="Limni Gölü Fotoğraf Albümü")
etiket.pack()

def ileri():
    if display == fotoğraf1:
        panel1.configure(image=fotoğraf2)
    else:
        panel1.configure(image= fotoğraf1)

ileributon = Button(album, text="İleri", font = ("Arial Black", 22), command=ileri)
ileributon.pack(side="right")

def geri():
    if display2 == fotoğraf2:
        panel1.configure(image = fotoğraf1)
    else:
        panel1.configure(image = fotoğraf2)

geributon = Button(album, text="Geri", font = ("Arial Black", 22), command=geri)
geributon.pack(side="left")

panel1 = Label(album, image=fotoğraf1)
display = fotoğraf1
panel1.pack(side="top")

panel2 = Label(album, image=fotoğraf2)
display2 = fotoğraf2


album.mainloop()
