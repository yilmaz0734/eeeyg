print("""**************************************
      Hesap Makinesi
    İşlemler
     1. Toplama
     2. Çıkarma
     3. Çarpma
     4. Bölme
        *************************************""")
a = int(input("Birinci sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))
işlem=(input("İşlemi giriniz: "))
if işlem=="1":
    print("{} ve {}'nın toplamı {}'dır.".format(a,b,a+b))
elif işlem=="2":
    print("{} ve {}'nın farkı {}'dır.".format(a,b,a-b))
elif işlem=="3":
    print("{} ve {}'nın çarpımı {}'dır.".format(a,b,a*b))
elif işlem=="4":
    print("{} ve {}'nın bölümü {}'dır.".format(a,b,a/b))

    input("dlekwkcec")

