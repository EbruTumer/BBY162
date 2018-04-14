import random
from tkinter import Tk, Label, Button
class benimİlkUygulamam:
    def __init__(self, master):
        self.master = master
        master.title("Ebru Tümer")

        self.label = Label(master, text="Günüz Sözü")
        self.label.pack()

        self.selam_button = Button(master, text="Selam", command=self.selam)
        self.selam_button.pack()

        self.gününSözünüSeç = Button(master, text= "Sözü Göster", command= self.gününSözü)
        self.gününSözünüSeç.pack()

        self.kapatma_button = Button(master, text="Çıkış", command=master.quit)
        self.kapatma_button.pack()

        def selam(self):
            print("Selamlar!")

        def gününSözü(self):
            sözler = ["Acı veriyorsa geçmiş; geçmemiş demektir.", "Parası olan pazardan, imanı olan mezardan korkmaz.", "Sevmek, bir başkasının hayatını yaşamaktır."]
            secilenSöz = random.choice(sözler)
            self.sözüm = Label(self.sözüm, text= secilenSöz)
            self.sözüm.pack()



