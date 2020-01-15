sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
sayi3=int(input("Üçüncü sayıyı giriniz: "))
if sayi1>sayi2 and sayi1>sayi3:
    print(sayi1,"(ilk sayı)")
elif sayi2>sayi1 and sayi2>sayi3:
    print(sayi2,"(ikinci sayı)")
else:
    print(sayi3,"(üçüncü sayı)")