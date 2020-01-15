a=int(input("Bir sayı giriniz:"))
faktoriyel=1
liste=list(range(2,a+1))
for i in liste:
    faktoriyel*=i
print(faktoriyel)