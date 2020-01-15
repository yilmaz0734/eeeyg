def asal_mi(sayı):
    i=2
    if sayı==1:
        return False
    elif sayı==2:
        return True
    elif sayı%2==1:
        while i<sayı:
            if sayı%i==0:
                return False
            i+=1
        return True
    else:
        return False

print(asal_mi(9))
                
                



