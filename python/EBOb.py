a=int(input("Birinci sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))
liste1=list()
def ebob(sayı1,sayı2):
    for i in range(1,sayı2+1):
        if sayı1%i==0 and sayı2%i==0:
            liste1.append(i)
    return max(liste1)
print(ebob(a,b))


