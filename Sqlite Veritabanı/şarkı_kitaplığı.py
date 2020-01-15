import sqlite3
import time


class sarki():


    def __init__(self,isim,sanatci,album,produktor,sure):

        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.produktor=produktor
        self.sure=sure

    def __str__(self):

        return "Şarkı adı: {} \nSanatçı: {} \nAlbüm: {} \nProdüktör: {} \nSüre: {}\n".format(self.isim,self.sanatci,self.album,self.produktor,self.sure)



class sarkikitapligi():


    def __init__(self):

        self.baglanti()

    def baglanti(self):

        self.baglanti = sqlite3.connect("sarkilar.db")
        self.islemci = self.baglanti.cursor()
        sorgu="Create table if not exists şarkılarr (İsim TEXT,Sanatçı TEXT,Albüm TEXT,Prodüksiyon Şirketi TEXT,Şarkı Süresi REAL)"

        self.islemci.execute(sorgu)
        self.baglanti.commit()

    def sarkiekle(self,sarki):

        self.islemci.execute("Insert into şarkılarr values(?,?,?,?,?)",(sarki.isim,sarki.sanatci,sarki.album,sarki.produktor,sarki.sure))
        self.baglanti.commit()

    def sarkisil(self,sarki):

        self.islemci.execute("Delete from şarkılarr where İsim= ?",(sarki.isim,))
        self.baglanti.commit()

    def sarkisorgula(self,sarki):

        self.islemci.execute("Select * form şarkılarr where İsim= ?",(sarki.isim,))
        liste=self.islemci.fetchall()

        for i in liste:

            print(i)

    def sanatcisorgula(self,sanatci):

        self.islemci.execute("Select * from şarkılarr where Sanatçı=?",(sanatci,))
        liste2=self.islemci.fetchall()

        for i in liste2:

            print(i)

    def toplamsure(self):

        self.islemci.execute("Select Şarkı Süresi from şarkılarr")
        liste1=self.islemci.fetchall()

        a=0

        for i in liste1:

            a+=i[0]

        print(a)




