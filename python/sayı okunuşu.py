a=int(input("İki basamaklı bir sayı giriniz: "))
def okunuş(sayı):
    if int(sayı)//10==1:
        if int(sayı)%10==1:
            print("On bir")
        elif int(sayı)%10==2:
            print("On iki")
        elif int(sayı)%10==3:
            print("On üç")
        elif int(sayı)%10==4:
            print("On dört")
        elif int(sayı)%10==5:
            print("On beş")
        elif int(sayı)%10==6:
            print("On altı")
        elif int(sayı)%10==7:
            print("On yedi")
        elif int(sayı)%10==8:
            print("On sekiz")
        else:
            print("On dokuz")
    elif int(sayı)//10==2:
        if int(sayı)%10==1:
            print("Yirmi bir")
        elif int(sayı)%10==2:
            print("Yirmi iki")
        elif int(sayı)%10==3:
            print("Yirmi üç")
        elif int(sayı)%10==4:
            print("Yirmi dört")
        elif int(sayı)%10==5:
            print("Yirmi beş")
        elif int(sayı)%10==6:
            print("Yirmi altı")
        elif int(sayı)%10==7:
            print("Yirmi yedi")
        elif int(sayı)%10==8:
            print("Yirmi sekiz")
        else:
            print("Yirmi dokuz")
    elif int(sayı)//10==3:
        if int(sayı)%10==1:
            print("Otuz bir")
        elif int(sayı)%10==2:
            print("Otuz iki")
        elif int(sayı)%10==3:
            print("Otuz üç")
        elif int(sayı)%10==4:
            print("Otuz dört")
        elif int(sayı)%10==5:
            print("Otuz beş")
        elif int(sayı)%10==6:
            print("Otuz altı")
        elif int(sayı)%10==7:
            print("Otuz yedi")
        elif int(sayı)%10==8:
            print("Otuz sekiz")
        else:
            print("Otuz dokuz")

okunuş(a)