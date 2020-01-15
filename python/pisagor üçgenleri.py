from typing import List, Any

liste=list()
c=int
def pisagor():
    for a in range(1,101):
        for b in range(1,101):
            if (a**2+b**2)**0.5==c:
                if c==int(c):
                    liste.append(a,b,int(c))
                    return liste
print(pisagor())