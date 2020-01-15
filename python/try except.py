def çiftmi(sayı):
    if sayı%2==0:
        return sayı
    else:
        raise ValueError("Çift değil bu sayı")
liste=[1,2,3,4,5,6,7,8,9]
for i in liste:
    try:
        çiftmi(i)
        print(i)
    except:
        pass