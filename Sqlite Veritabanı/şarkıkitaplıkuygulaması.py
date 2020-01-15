from şarkı_kitaplığı import *
print(''' *************************************** 
Şarkı Kütüphanesine Hoş Geldiniz!
1. Şarkı Ekle
2. Şarkı Sorgula
3. Şarkı Sil
4. Kütüphanenin Toplam Süresini Bul
5. Sanatçı Sorgula
Not: Çıkmak için 'q' ya basınız.
        ******************************************''')
while True:
    işlem=input("İşleminizi seçiniz: ")
    if işlem=="1":
        print("İşlem gerçekleştiriliyor...")
        time.sleep(1)
        print("Eklemek istediğiniz şarkının özelliklerini giriniz")
        time.sleep(1)
        isim=input("Şarkı adı: ")
        sanatçı=input("Sanatçı adı: ")
        albüm=input("Albüm adı: ")
        prodüktör=input("Prodüktör adı: ")
        süre=input("Süresi: ")
        print("Ekleniyor...")
        time.sleep(2)
        şarkım=sarki(isim,sanatçı,albüm,prodüktör,süre)
        sarkikitapligi().sarkiekle(şarkım)
        print("Eklendi.")
    elif işlem=="2":
        print("İşlem gerçekleştiriliyor...")
        time.sleep(1)
        a=input("Hangi şarkıya bakmıştınız: ")
        print("Sorgulanıyor...")
        time.sleep(2)
        sarkikitapligi().sarkisorgula(a)


    elif işlem=="3":
        print("İşlem gerçekleştiriliyor...")
        time.sleep(1)
        b=input("Silmek istediğiniz şarkıyı giriniz: ")
        print("Siliniyor...")
        sarkikitapligi().sarkisil(b)
        time.sleep(2)
        print("Silindi.")

    elif işlem=="4":
        print("Hesaplanıyor...")
        time.sleep(1)
        sarkikitapligi().toplamsure()
    elif işlem=="5":
        c=input("Hangi sanatçıya bakmıştınız: ")
        print("Bulunuyor...")
        time.sleep(2)
        sarkikitapligi().sanatcisorgula(c)
    elif işlem=="q":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Bir daha bekleriz!")
        break
    else:
        print("Hatalı işlem.")











