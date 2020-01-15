import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tabloyuyarat():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,yazar TEXT,yayınevi TEXT,sayfa sayısı INT) ")
    con.commit()
def veriekleme():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()
def veriekleme2(isim,yazar,yayınevi,sayfasayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfasayısı))
    con.commit()
isim=input("Kitabın ismini giriniz: ")
yazar=input("Yazarın ismini giriniz: ")
yayınevi=input("Yayınevini giriniz: ")
sayfasayısı=input("Sayfa sayısını giriniz: ")
veriekleme2(isim,yazar,yayınevi,sayfasayısı)

con.close()
