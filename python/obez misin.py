while True:
    kilo=float(input("Kilonuzu giriniz: "))
    boy=float(input("Boyunuzu giriniz: "))
    bki=kilo/boy**2
    if bki<18.5 :
        print("Zayıfsınız")
    elif 18.5<bki<25 :
        print("Normalsiniz")
    elif 25<bki<30:
        print("Fazla kilolusunuz")
    else :
        print("Obezsiniz")

