liste=list()
def futbolcular(satır):
    satır=satır[:-1]
    liste=satır.split(",")
    isim=liste[0]
    return isim
with open("fb.txt","r",encoding="utf-8") as