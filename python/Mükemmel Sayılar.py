
def tambolenler(sayı):
    for i in range(1,sayı):
        if sayı%i==0:
            liste.append(i)
    print(liste)
    return sum(liste)
while True:
    liste=list()
    sayı=int(input("Bir sayı giriniz: "))
    if sayı==tambolenler(sayı):
        print("Mükemmel sayıyı buldunuz.")
    else:
        print("Bu mükemmel bir sayı değil.")
