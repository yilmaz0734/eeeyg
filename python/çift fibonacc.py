a=1
b=1
c=2
liste=list()
while (a and b and c)<4000000:
    if a%2==0:
        liste.append(a)
    if b%2==0:
        liste.append(b)
    if c%2==0:
        liste.append(c)
    a = b + c
    b = a + c
    c = a + b
print(liste)
toplam=sum(liste)
print("toplam" , toplam)
