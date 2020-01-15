# yapmam gereken şey 1'den 1000'e kadar 3 ve 5'in katlarının toplamını bulmak 1000/3=333, 1000/5=200... İf kodu ile yazmak kolay
a=0
b=0
liste1=list()
liste2=list()
liste3=list()
while int(a)<1000:
    if a%3!=0:
        a+=1
        continue
    liste1.append(a)
    a+=1
while int(b)<1000:
    if b%5!=0:
        b+=1
        continue
    liste2.append(b)
    b+=1
liste1.extend(liste2)
toplam1=sum(liste1)
print(toplam1)
c=0
while int(c)<1000:
    if c%15!=0:
        c+=1
        continue
    liste3.append(c)
    c+=1
toplam2=sum(liste3)
toplam=toplam1-toplam2
print(toplam)


