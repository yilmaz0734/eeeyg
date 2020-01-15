a=str(input("Bir sayı giriniz: "))
basamak=len(a)
liste=list(a)
üslü=1
toplam=0
for i in liste:
    üslü=int(i)**int(basamak)
    toplam+=üslü
if toplam==int(a):
    print("Armstrong sayısını buldunuz.")
else:
    print("Armstrong sayısı değil bu.")
