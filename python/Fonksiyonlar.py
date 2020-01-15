def asalmi(sayı):
    if sayı==1:
        return False
    elif sayı==2:
        return True
    else:
        for i in range(2,sayı):
            if sayı%i==0:
                return False
        return True

print(asalmi(147977))
liste=list()

def tambolenler(sayı2):
    for k in range(2,sayı2+1):
        if sayı2%k==0 and asalmi(k)==True:
            liste.append(k)
    print(liste)
tambolenler(147977)


