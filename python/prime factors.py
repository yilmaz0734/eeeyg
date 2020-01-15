c=600851475143
liste=list()
liste1=list()
for eleman in range(1,c):
    if eleman>1:
        for i in range(2,(eleman)):
            if eleman%i==0:
                break
        else:
            liste.append(eleman)
for i in liste:
    if c%i==0:
        liste1.append(i)

print(liste1)
