from tkinter import *
import tkinter
import random


temel = tkinter.Tk()
fr = tkinter.Frame(temel, bg="black", width="238", height="250")

puan = tkinter.Label(temel, bg="black", fg="white", text="Puan:")
puan.place(x = 30, y = 15)

p=0

puan_numarası = tkinter.Label(temel, bg="black", fg="white", text = p)
puan_numarası.place(x = 70, y = 15)

skor = tkinter.Label(temel, bg="black", fg="white", text="Skor:")
skor.place(x = 155, y = 15)

s = 0

eniyi_skor = tkinter.Label(temel, bg="black", fg="white", text = s)
eniyi_skor.place(x = 188, y = 15)

tıklama = []
renk = 0

def yellowtıklama():

    yellow.configure(activebackground="yellow3")
    yellow.after(500, lambda: yellow.configure(activebackground="yellow"))

    global tıklama
    global renk

    renk = 1
    tıklama.append(renk)

yellow = tkinter.Button(temel, bd="0", highlightthickness="0",width="7",
                        height="5", activebackground="yellow",
                        bg="yellow3", command = yellowtıklama)

yellow.place(x = 30, y = 50)

def bluetıklama():

    blue.configure(activebackground="dark blue")
    blue.after(500, lambda: blue.configure(activebackground="blue"))

    global tıklama
    global renk

    renk = 2
    tıklama.append(renk)

blue = tkinter.Button(temel, bd="0", highlightthickness="0",width="7", height="5",
                      activebackground="blue",
                      bg="dark blue", command = bluetıklama)
blue.place(x = 125, y = 50)

def redtıklama():

    red.configure(activebackground="red3")
    red.after(500, lambda: red.configure(activebackground="red"))

    global tıklama
    global renk

    renk = 3
    tıklama.append(renk)

red = tkinter.Button(temel, bd="0", highlightthickness="0", width="7", height="5",
                     activebackground="red",
                     bg = "red3", command = redtıklama)

red.place(x = 30, y = 145)

def greentıklama():

    green.configure(activebackground="dark green")
    green.after(500, lambda: green.configure(activebackground="green4"))

    global tıklama
    global renk

    renk = 4
    tıklama.append(renk)

green = tkinter.Button(temel, bd="0", highlightthickness="0",width="7", height="5",
                       activebackground="green4",
                       bg="dark green", command = greentıklama)

green.place(x = 125, y = 145)

def sayıYapmak():

    global p
    p = p + 1
    puan_numarası.configure(text = p)

i = random.randint(1, 4)

sıra = []

def checkSıra():

    global tıklama
    global sıra

    if tıklama == sıra:
        sayıYapmak()
def sıraGöster():

    global i
    global sıra

    if i == 1:

        yellow.configure(bg="yellow")
        yellow.after(500, lambda: yellow.configure(bg="yellow3"))
        sıra.append(i)
        temel.after(5000, checkSıra)

    elif i == 2:

        blue.configure(bg="blue")
        blue.after(500, lambda: blue.configure(bg="dark blue"))
        sıra.append(i)
        temel.after(5000, checkSıra)

    elif i == 3:

        red.configure(bg="red")
        red.after(500, lambda: red.configure(bg="red3"))
        sıra.append(i)
        temel.after(5000, checkSıra)

    elif i == 4:

        green.configure(bg="green4")
        green.after(500, lambda: green.configure(bg="dark green"))
        sıra.append(i)
        temel.after(5000, checkSıra)

temel.after(2000, sıraGöster)

buton1=tkinter.Button(temel,text="Kontrol Et")
buton1.pack(side="bottom")

buton2= tkinter.Button(temel, text="Oyuna Başla")
buton2.pack(side="bottom")

fr.pack()
temel.resizable(0, 0)
temel.mainloop()