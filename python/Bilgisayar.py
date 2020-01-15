img1="image1"
img2="image2"
img3="image3"
img4="image4"
img5="image5"
resimlerim=[img1,img2,img3,img4,img5]
GTA5="GTA 5"
MountandBlade="Mount and Blade"
CSGO="Counter Strike Global Offensive"
Witcher3="Witcher 3"
oyunlarım=[GTA5,MountandBlade,CSGO,Witcher3]
belge1="Öğrenci Belgesi"
belge2="CV"
belge3="Ödev-Fizik"
belge4="Ödev-Matematik"
belgelerim=[belge1,belge2,belge3,belge4]
müzik1="Enginde Yavaş Yavaş"
müzik2="Veda Busesi"
müzik3="Hatırla Sevgili"
müzikler=[müzik1,müzik2,müzik3]
class bilgisayar():
    def __init__(self,açıkmıkapalımı="Kapalı",dosyalar=[resimlerim,oyunlarım,belgelerim,müzikler],ses=0):
        self.açıkmıkapalımı=açıkmıkapalımı
        self.dosyalar=dosyalar
        self.ses=ses
    def açkapa(self):
        if self.açıkmıkapalımı=="Kapalı":
            self.açıkmıkapalımı="Açık"
            print("Bilgisayar açıldı.")
        elif self.açıkmıkapalımı=="Açık":
            self.açıkmıkapalımı="Kapalı"
            print("Bilgisayar kapandı.")
    def dosyaaç(self):
        print(""" Dosyalar: 
        1.Resimlerim
        2.Oyunlarım
        3.Belgelerim
        4.Müzikler """)
        a=input("Dosya adını giriniz: ")
        if a=="1":
            print(resimlerim)
            b=input("Açmak istediğiniz resmi seçiniz: ")
            if b=="image1":
                print("İmg1 açıldı")
            elif b=="image2":
                print("img2 açıldı")
            elif b=="image3":
                print("img3 açıldı")
            elif b=="image4":
                print("img4 açıldı")
            elif b=="img5":
                print("image5 açıldı")
            else:
                print("Böyle bir resim bulunamadı.")
        elif a=="2":
            print(oyunlarım)
            c=input("Açmak istediğiniz oyunu seçiniz: ")
            if c=="GTA 5":
                print("GTA 5 açıldı.")
            elif c=="Mount and Blade":
                print("Mount and Blade açıldı.")
            elif c=="Counter Strike Global Offensive":
                print("CS:GO açıldı.")
            elif c=="Witcher 3":
                print("Witcher 3 açıldı.")
            else:
                print("Böyle bir oyun bulunamadı.")
        elif a=="3":
            print(belgelerim)
            d=input("Açmak istediğiniz belgeyi seçiniz: ")
            if d=="Öğrenci Belgesi":
                print("Öğrenci belgesi açıldı.")
            elif d=="CV":
                print("CV açıldı.")
            elif d=="Ödev-Fizik":
                print("Fizik ödevi açıldı.")
            elif d=="Ödev-Matematik":
                print("Matematik ödevi açıldı.")
            else:
                print("Böyle bir belge bulunamadı.")
        elif a=="4":
            print(müzikler)
            e=input("Açmak istediğiniz müzik: ")
            if e=="Enginde Yavaş Yavaş":
                print("Enginde yavaş yavaş açıldı.")
            elif e=="Hatırla Sevgili":
                print("Hatırla sevgili açıldı.")
            elif e=="Veda Busesi":
                print("veda busesi açıldı.")
            else:
                print("Böyle bir müzik bulunamadı.")
        else:
            print("Dosya bulunamadı.")
    def sesaçkapa(self):
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
print(""" Bilgisayara hoşgeldiniz...
Yapabileceğiniz işlemler aşağıda yazmaktadır:
1.Aç/Kapa
2.Dosyalara Gir
3.Ses Aç/Kapa   """)
bilgisayar1=bilgisayar()
while True:
    komut=input("İşlemi giriniz: ")
    if komut=="1":
        bilgisayar1.açkapa()
    elif komut=="2":
        bilgisayar1.dosyaaç()
    elif komut=="3":
        bilgisayar1.sesaçkapa()
    else:
        print("Böyle bir işlem bulunmamaktadır.")









        