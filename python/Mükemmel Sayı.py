
    liste=list()
    a=int(input("Bir sayı giriniz: "))
    for i in range(1,a):
        if a%i==0:
            liste.append(i)
    print(liste)
    if sum(liste)==a:
        print("Mükemmel sayıyı buldunuz!")
    else:
        print("Bu sayı mükemmel değil")
