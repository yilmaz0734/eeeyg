print(''' *******************************
            Çıkmak için q'ya basınız
          *******************************''')
a=1
while True:
    b=(input("Bir sayı giriniz: "))
    if b=="q":
        print("Çıkış yapılıyor...")
        break
    a*=int(b)
    print(a)
sonuc=a
print(sonuc)
