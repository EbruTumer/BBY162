import random

hayvanlar = random.choice(['orangutan', 'güvercin', 'gelincik', 'gergedan', 'balina', 'tavşan', 'panda', 'penguen', 'balık'])
harfhavuzu = []
can = 4
oyuncizgileri = '_'

oyuncizgisisayısı = list(oyuncizgileri * len(hayvanlar))

dongu = 1

while dongu:
    print(' '.join(oyuncizgisisayısı), end='\n\n')

    girilenharf = input('Bir harf giriniz: ').lower()

    try:
        int(girilenharf)
        print('Doğru bir şeyler girdiğinden emin ol.\n')
    except:
        if len(girilenharf) > 1:
            print('Harf giriniz!\n')
        else:
            if girilenharf in harfhavuzu:
                print('Bu harfi zaten girdiniz.\n')
            else:
                bulduk = None
                for i in range(len(hayvanlar)):
                    if girilenharf == hayvanlar[i]:
                        bulduk = True

                        oyuncizgisisayısı[i] = girilenharf

                        harfhavuzu.append(girilenharf)

                        if oyuncizgileri not in oyuncizgisisayısı:
                            print(' '.join(oyuncizgisisayısı))
                            print('\nTebrikler kelimeyi buldunuz!')

                            dongu = 0

                else:

                    if bulduk != True:
                        can -= 1

                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(can))

                        harfhavuzu.append(girilenharf)

                if can == 0:
                    print('Kaybettin. Doğru kelime "{}" idi.\n'.format(hayvanlar))

                    break

