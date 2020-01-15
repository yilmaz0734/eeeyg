import sqlite3
import time




class urun():


    def __init__(self,adı,adedi,fiyatı):

        self.adı=adı
        self.adedi=adedi
        self.fiyatı=fiyatı

    def __str__(self):

        return "Ürün adı: {} \nÜrün Adedi: {} \nÜrün Fiyatı: {} \n".format(self.adı,self.adedi,self.fiyatı)



class market():


    def __init__(self):

        self.baglantikur()

    def baglantikur(self):

        self.conn=sqlite3.connect("supermarket.db")
        self.cursor=self.conn.cursor()
        self.cursor.execute("Create table if not exists market (Ürün TEXT,Adet TEXT,Fiyat REAL)")
        self.conn.commit()
    def
