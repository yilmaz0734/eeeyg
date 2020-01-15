from kütüphane import *
kütüphane=kütüphane()
print("""***********************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil 

5. Baskı Yükselt

Çıkmak için 'q' ya basın.
***********************************""")

while True:


    islem=input("İşlemi giriniz:")


    if islem=="1":

        print("İşleminiz başlatılıyor..")
        time.sleep(2)
        kütüphane.kitaplarigoster()
        durdur=input("İşlemi sonlandırmak için 'q'a basınız... ")

        if durdur=="q":

            print("İşlem sonlandırılıyor..")
            time.sleep(1)

            break


    elif islem=="2":

        print("İşleminiz başlatılıyor..")
        time.sleep(2)
        kitab=input("Hangi kitaba bakmıştınız? : ")
        kütüphane.kitapsorgula(kitab)
        durdur2=input("İşlemi sonlandırmak için 'q'a basınız..")

        if durdur2=="q":
            print("İşleminiz sonlandırılıyor..")
            time.sleep(1)

            break


    elif islem=="3":

        print("İşleminiz başlatılıyor..")
        time.sleep(2)
        print("Eklemek istediğiniz kitap bilgilerini giriniz: ")
        isim=input("İsim: ")
        yazar=input("Yazar: ")
        yayınevi=input("Yayınevi: ")
        tür=input("Tür: ")
        baskı=input("Baskı: ")
        kitabıhikmet=kitap(isim,yazar,yayınevi,tür,baskı)
        kütüphane.kitapekle(kitabıhikmet)
        a=input("Kitap eklendi, çıkmak için 'q'ya basınız...")

        if a=="q":

            print("İşlem sonlandırılıyor...")
            time.sleep(1)

            break


    elif islem=="4":

        print("İşleminiz başlatılıyor...")
        time.sleep(2)
        isim=input("Silmek istediğiniz kitap adını giriniz: ")
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(2)
        kütüphane.kitapsil(isim)
        k=input("İşleminiz gerçekleştirildi, çıkmak için 'q'ya basınız...")

        if k=="q":

            print("İşlem sonlandırılıyor...")
            time.sleep(1)

            break


    elif islem=="5":

        print("İşleminiz başlatılıyor..")
        time.sleep(1)
        issim=input("Baskısını yükseltmek istediğiniz kitabın ismini giriniz: ")
        print("İşleminiz gerçekleştiriliyor...")
        time.sleep(2)
        kütüphane.baskiyukselt(issim)
        kl=input("İşleminiz gerçekleştirildi, çıkmak için 'q'ya basınız...")

        if kl=="q":

            print("İşlem sonlandırılıyor...")
            time.sleep(1)

            break
    else:

        print("Lütfen geçerli bir işlem giriniz...")

        break












