print(" **************************************\n"
      "      Girdiğiniz şekli belirtmelisiniz \n"
      "     1.Üçgen\n"
      "        2.Dörtgen\n"
      "      ****************************************")
sekil=input("Şekil: ")
if sekil=="1" :
    kenar1=float(input("Kenar 1: "))
    kenar2=float(input("Kenar 2: "))
    kenar3=float(input("Kenar 3: "))
    if abs(kenar2-kenar3)<kenar1<kenar2+kenar3 and abs(kenar1-kenar3)<kenar2<kenar1+kenar3 and abs(kenar1 - kenar2)<kenar3<kenar1+kenar2:
        if kenar1==kenar2==kenar3:
            print("Eşkenar üçgeniniz hayırlı olsun.")
        elif kenar1==kenar2 or kenar1==kenar3 or kenar2==kenar3:
            print("İkizkenar üçgeniniz hayırlı olsun.")
        else:
            print("Çeşitkenar üçgeniniz hayırlı olsun.")
    else:
        print("Çizdiğiniz şey bir üçgen değil.")
elif sekil=="2":
    kenaar1=float(input("Kenar 1'i giriniz: "))
    kenaar2=float(input("Kenar 2'yi giriniz: "))
    kenaar3=float(input("Kenar 3'ü giriniz: "))
    kenaar4=float(input("Kenar 4'ü giriniz: "))
    if kenaar1==kenaar2==kenaar3==kenaar4:
        print("Kare çizdiniz.")
    elif kenaar1==kenaar3 or kenaar2==kenaar4:
        print("Dikdörtgeniniz hayırlı olsun.")
    else:
        print("Çok şekilsiz bir dörtgen oldu bu.")
else:
    print("Adamakıllı bir şey çizin lütfen.")
