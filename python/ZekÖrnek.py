with open("metin.txt","r",encoding="utf-8") as zek:
    içerik=zek.read()
    içerik=içerik.strip(",")
    içerik=içerik.strip(".")
    içerik=içerik.strip("\n")
    liste=list()
    kelimeler=içerik.split(" ")
    
    for i in kelimeler:
        liste.append(i)
    sözlük=dict()
    for j in liste:
        if j in sözlük:
            sözlük[j]+=1
        else:
            sözlük[j]=1
    for kelime,sayı in sözlük.items():

        print("{} kelimesi {} kadar geçti.".format(kelime,sayı))
        
    