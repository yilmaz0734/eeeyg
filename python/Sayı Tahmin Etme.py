import random
import time
print(""""
      *************************
      Bir ile kırk arasında bir sayı tahmin et!
5 Hakkın var.
*************************
    """)
dorusayi=random.randint(1,40)
tahmin=5
while True:
    tahmin=int(input("Tahmininiz: "))
    if tahmin<dorusayi:
        print("Bilgiler sorgulanıyor...")
        time.sleep(3)
        print("Sayıyı artır.")
    elif tahmin==dorusayi:
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Tutturdun!")
        break
    else:
        print("Bilgiler sorgulanıyor.")
        time.sleep(3)
        print("Sayıyı azalt.")
