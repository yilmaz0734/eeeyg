import sqlite3
import time
class kitap():
    def __init__(self,isim,yazar,yayınevi,tür,baskı):
        self.isim=isim
        self.yazar=yazar
        self.yayınevi=yayınevi
        self.tür=tür
        self.baskı=baskı
    def __str__(self):
        return "Kitap ismi: {}\nYazarı: {}\nYayınevi: {}\nTürü: {}\nBaskı: {}".format(self.isim,self.yazar,self.yayınevi,self.tür,self.baskı)


class kütüphane():
    def __init__(self):
        self.baglantikur()
    def baglantikur(self):
        self.baglanti=sqlite3.connect("kütüphane.db")
        self.cursor=self.baglanti.cursor()
        sorgu="CREATE TABLE IF NOT EXISTS kitaplar(isim TEXT,yazar TEXT,yayınevi TEXT,tür TEXT,baskı INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()


    def baglantikes(self):
        self.baglanti.close()


    def kitaplarigoster(self):
        self.sorgu2="Select * from kitaplar"
        self.cursor.execute(self.sorgu2)
        self.kitaplar=self.cursor.fetchall()

        if len(self.kitaplar)==0:

            print("Kütüphanede kitap yok")

        else:

            for i in self.kitaplar:
                Kitap=kitap(i[0],i[1],i[2],i[3],i[4])
                print(Kitap)


    def kitapsorgula(self,isim):
        self.sorgu3="Select * from kitaplar where isim=?"
        self.cursor.execute(self.sorgu3,(isim,))
        kitapliste=self.cursor.fetchall()

        if len(kitapliste)==0:

            print("Böyle bir kitap bulunmuyor.")

        else:

            Kitabım=kitap(kitapliste[0][0],kitapliste[0][1],kitapliste[0][2],kitapliste[0][3],kitapliste[0][4])
            print(Kitabım)


    def kitapekle(self,kitap):
        sorgu="Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.baskı,kitap.tür))
        self.baglanti.commit()


    def kitapsil(self,isim):
        sorgu="Delete from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()


    def baskiyukselt(self,isim):
        sorgu="Select * from kitaplar where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitabliste=self.cursor.fetchall()
        if len(kitabliste)==0:
            print("Böyle bir kitap bulunmuyor.")
        else:
            baskı=kitabliste[0][4]
            baskı+=1
            sorgu2="Update kitaplar set baskı=? where isim=?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.baglanti.commit()


kütüphane().kitaplarigoster()
