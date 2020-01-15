import time
import random
print(""" Kumandaya hoşgeldiniz...
Yapabileceğiniz işlemler aşağıda yazmaktadır:
1.TV'yi aç/kapa.
2.Sesi artır/azalt.
3.Listeye kanal ekle.
4. Rasgtele bir kanala geçiş yap. """)
class kumanda():
    def __init__(self,açkapa="Kapalı",ses=0,kanallar=list(),kanal="TRT"):
        self.açkapa=açkapa
        self.ses=ses
        self.kanallar=kanallar
        self.kanal=kanal
    def açma(self):
        if self.açkapa == "Kapalı":
            self.açkapa == "Açık"
            print("Televizyon açıldı.")
        elif self.açkapa=="Açık":
            self.açkapa == "Kapalı"
            print("Televizyon kapandı.")

    def sesartırma(self):
        print("Sesi açmak için '>', azaltmak için '<' tuşuna basınız.")
        time.sleep(1)
        a=input("Buyrun: ")
        while 0<=self.ses<32:
            if a==">":
                self.ses+=1
                print("Ses: ",self.ses)
                break
            elif a=="<":
                if self.ses==0:
                    print("Ses zaten 0")
                    self.ses=0
                    break
                else:
                    self.ses-=1
                    break
                print("Ses: ",self.ses)
            else:
                print("Yanlış komut.")
                break
    def kanalekleme(self):
        print("Şu anki kanal listesi: ", self.kanallar)
        time.sleep(1)
        print("Kanal eklemek için ekleyeceğiniz kanalın adını giriniz.")
        time.sleep(2)
        b=input("Kanalınız: ")
        self.kanallar.append(b)
        print("Yeni kanal listesi: ",self.kanallar)
    def rastgelekanalagec(self):
        print("Kanalınız: ",random.randint(1,len(self.kanallar)))
kumanda1=kumanda()
time.sleep(3)
while True:
    c=input("İşlemi belirtiniz: ")
    if c=="1":
        print("İşlem yapılıyor..")
        time.sleep(1)
        kumanda1.açma()
    elif c=="2":
        print("İşlem yapılıyor..")
        time.sleep(1)
        kumanda1.sesartırma()
    elif c=="3":
        print("İşlem yapılıyor..")
        time.sleep(1)
        kumanda1.kanalekleme()
    elif c=="4":
        print("İşlem yapılıyor..")
        time.sleep(1)
        kumanda1.rastgelekanalagec()
    else:
        print("Yanlış komut girildi.")









