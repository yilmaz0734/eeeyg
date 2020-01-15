with open("metin.txt","r",encoding="utf-8") as file:
    içerik=file.read()
    içerik=içerik.strip(",")
    içerik=içerik.strip(".")
    kelimeler=içerik.split(" ")
    sözlük=dict()
    for i in kelimeler:
        if i in sözlük:
            sözlük[i]+=1
        else:
            sözlük[i]=1
    for kelime,sayı in sözlük.items():
        print("{} kelimesi {} kadar geçti.".format(kelime,sayı))
            


        
    