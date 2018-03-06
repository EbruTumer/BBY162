sınavlar= input("Notunuzu giriniz: ")
if int(sınavlar)< 50:
        print("Notunuz 0 ile 50 arasında, tehlikedesiniz.")
elif 50< int(sınavlar) < 100:
        print("Notunuz 50 ile 100 arasında, gayet güzel.")
else:
    print("0-100 arası bir değer girin.")
