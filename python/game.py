T=input()
for i in range(int(T)):
   A=input()
   B=input()
   N=int(B)-int(A)
   for j in range(A+1,B+1):
        donut=input()
        if donut=="TOO_SMALL":
            for x in range(j+1,B+1):
                continue
        elif donut=="TOO_BIG":
            for k in range(A+1,j):
                continue
        elif donut=="CORRECT":
            print(j)
            break