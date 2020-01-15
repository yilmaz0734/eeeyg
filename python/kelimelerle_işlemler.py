class yılmaz():

    def __init__(self):

        with open("metin.txt","r",encoding="utf-8") as file:

            içerik=file.read()
            kelimeler=içerik.split()
            self.kelimelistesi=list()
            for j in kelimeler:
                j=j.strip("\n")
                j=j.strip(" ")
                j=j.strip(",")
                j=j.strip(".")
                self.kelimelistesi.append(j)
           
    def tumkelimeler(self):
        self.sadekelimeler=set()
        for i in self.kelimelistesi:
            self.sadekelimeler.add(i)
        print(self.sadekelimeler)
    
    def kelimefrekans(self):
        self.kelimefrekansı=dict()
        for i in self.kelimelistesi:
            if i in self.kelimefrekansı:
                self.kelimefrekansı[i]+=1
            else:
                self.kelimefrekansı[i]=1
        for kelime,sayı in self.kelimefrekansı.items():
            print("{} kelimesi {} kere geçti".format(kelime,sayı))


