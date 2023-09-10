#Bu örneğimizde Python ile taş kağıt makas oyunu kodlaması yapılacaktır. Oyunun kazanma şartları aşağıdaki şekilde belirlenmiştir.
#Taş, makası kırarak yener.
#Kağıt, taşı sararak yener.
#Makas, kağıdı keserek yener.
import random

tas = 1
kagit = 2
makas = 3

sayacBilgisayar = 0
sayacOyuncu = 0

while((sayacBilgisayar or sayacOyuncu)!= 3):
    bilgisayar = random.randint(1, 3)
    try:
        oyuncu = int(input("Bİr tahmin giriniz:"))
        if (oyuncu != 1 and oyuncu != 2 and oyuncu != 3):
            print("Geçersiz değer! 1,2 ve 3 dışında bir sayı girmeyin...")
            continue
    except ValueError:
        print("Geçersiz değer! 1,2 ve 3 dışında bir sayı girmeyin...")
        continue


    if (bilgisayar == 1 and oyuncu == 1) or (bilgisayar == 2 and oyuncu == 2) or (bilgisayar == 3 and oyuncu == 3):
        print("Berabere")

    elif (bilgisayar == 1 and oyuncu == 2):
        print("Kağıt taşı sararak yener\noyuncu kazandı.")

    elif (bilgisayar == 2 and oyuncu == 3):
        print("Makas kağıdı keserek yener\noyuncu kazandı.")

    elif (bilgisayar == 3 and oyuncu ==1):
        print("Taş, makası kırarak yener\noyuncu kazandı.")

    elif (bilgisayar == 1 and oyuncu == 3):
        print("Taş, makası kırarak yener\nbilgisayar kazandı.")

    elif (bilgisayar == 2 and oyuncu == 1):
        print("Kağıt taşı sararak yener\nbilgisayar kazandı.")

    elif (bilgisayar == 3 and oyuncu == 2):
        print("Makas kağıdı keserek yener\nbilgisayar kazandı.")

    if (bilgisayar == 1 and oyuncu == 2) or (bilgisayar == 2 and oyuncu == 3) or (bilgisayar == 3 and oyuncu == 1):
        sayacOyuncu += 1
        sayacBilgisayar += 0

    if (bilgisayar == 1 and oyuncu == 3) or (bilgisayar == 2 and oyuncu == 1) or (bilgisayar == 3 and oyuncu == 2):
        sayacBilgisayar += 1
        sayacOyuncu += 0

    if (bilgisayar == 1 and oyuncu == 1) or (bilgisayar == 2 and oyuncu == 2) or (bilgisayar == 3 and oyuncu == 3):
        sayacBilgisayar += 0
        sayacOyuncu += 0
    print(f"Oyuncu: {sayacOyuncu} Bilgisayar: {sayacBilgisayar}")
    if sayacBilgisayar == 3:
        print("Üzgünüm Kaybettiniz...")
        break
    if sayacOyuncu == 3:
        print("Tebrikler Kazandınız...")
        break







