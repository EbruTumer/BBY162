import random
from tkinter import * #yıldız kullanıdığımızda otomatik tüm fonksiyonları tanımlıyor..

class benimİlkUygulamam:
    def __init__(self, master):
        self.master = master
        master.title("Ebru Tümer")
        master.configure(background="pink")

        self.label = Label(master, text="Günüz Sözü")
        self.label.pack()

        self.selam_button = Button(master, text="Selam", font = ("arial", 20), command=self.selam)
        self.selam_button.pack()

        self.gününSözünüSeç = Button(master, text= "Sözü Göster", font = ("castellar", 22), command= self.gününSözü)
        self.gününSözünüSeç.pack(side = "left")

        self.kapatma_button = Button(master, text="Çıkış", font= ("arial", 20), command=master.quit)
        self.kapatma_button.pack(side="bottom")

    def selam(self):
            print("Selamlar!")

    def gününSözü(self):
            sözler = ("Acı veriyorsa geçmiş; geçmemiş demektir.", "Parası olan pazardan, imanı olan mezardan korkmaz.", "Sevmek, bir başkasının hayatını yaşamaktır.", "Mutluluğu herkesle paylaşabilirsin ama acıyı paylaştığın insanlar özeldir.", "Ağlamak dudakların diyemediğini gözyaşlarına söyletmektir.")
            secilenSöz = random.choice(sözler)
            self.sözüm = Label(self.master, text=secilenSöz)
            self.sözüm.pack()

root = Tk()
my_gui = benimİlkUygulamam(root)
root.mainloop()
