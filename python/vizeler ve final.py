vize1=int(input("birinci vizenizi giriniz: "))
vize2=int(input("ikinci vizenizi giriniz: "))
final=int(input("final notunuzu giriniz: "))
ortalama=(vize1*3+vize2*3+final*4)/10
if ortalama>90:
    print("AA aldın aferin")
elif 55<ortalama<90:
    print("Geçtin.")
else:
    print("Kaldın la:(")