T=input()
for i in range(int(T)):
    b=input()
    c=b.split(" ")
    A=c[0]
    B=c[1]
    N=int(B)-int(A)
    for x in range(int(A)+1,int(B)+1):
        while N>0:
            N-=1
            
            donut=input()
            
            if donut=="TOO_SMALL":
                for j in range(x,int(B)+1):
                    print(j)
                    
            elif donut=="TOO_BIG":
                for k in range(int(A)+1,x+1):
                    print(k)
            elif donut=="CORRECT":
                print(x)

