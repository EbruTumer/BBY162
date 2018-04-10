__author__ = "Ebru Tümer"
#10.04.2018
import random
kalanHak = 3
i = 0
hayvanlar = random.choice(['orangutan', 'güvercin', 'gelincik', 'gergedan', 'balina', 'tavşan', 'panda', 'penguen', 'balık'])
harfHavuzu = []
print("Adam Asmaca Oyununa hoşgeldiniz!")
for kelime in hayvanlar:
    harfHavuzu.append("*")
print(harfHavuzu)
while kalanHak > 0:
    istenilenHarf = input("Lütfen bir harf giriniz: ").lower()
    if istenilenHarf in hayvanlar:
        for kontrol in hayvanlar:
            if hayvanlar [i] == istenilenHarf:
                harfHavuzu [i] = istenilenHarf
            i+=1
        print(harfHavuzu)
        print("Tebrikler, doğru harf!")
        i=0
    kontrol = istenilenHarf in hayvanlar
    if kontrol == False:
        kalanHak-=1
    print("Kalan hakkınız: ", str(kalanHak))
    i=0
if kalanHak == 0:
    print('Oyunu kaybettiniz! Doğru kelime "{}" idi.\n'.format(hayvanlar))