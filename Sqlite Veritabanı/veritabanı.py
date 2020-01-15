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
def veriçekme():
    cursor.execute("Select * from kitaplık")
    liste=cursor.fetchall()
    print(liste)
def belirliveri():
    cursor.execute("Select isim,yazar from Kitaplık")
    liste=cursor.fetchall()
    for i in liste:
        print(i)
def seciliveri(yayınevi):
    cursor.execute("Select * from kitaplık where yayınevi=?",(yayınevi,))
    liste=cursor.fetchall()
    print(liste)
def veriguncelle(eski,yeni):
    cursor.execute("Update kitaplık set yayınevi=? where yayınevi=?",(yeni,eski,))
    con.commit()
def verisil(yayınevi):
    cursor.execute("Delete from kitaplık where yayınevi=?",(yayınevi,))
    con.commit()
                


verisil("İnkılap Kitabevi")
con.close()
