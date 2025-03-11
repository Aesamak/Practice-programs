m=10
n=12#row always odd
lis=[]
lis1=[]
main=[]
h=n//2
h+=1
i=1
while i<=1 :
    for j in range(1,h+1):
        lis=[]
        lis1=[]
        b=1
        while b<=h:
            if j==b:
                for d in range(b,h+1):
                    lis.append(j)
                    b+=1
                
            else:
                for c in range(1,j):
                    lis.append(c)
                    b+=1    
            lis1=lis
        e=h
        while e>0:
            lis1.append(lis[e-1])
            e-=1  
        main.append(lis1)
    q=(h-2)
    for j in range(h+1,n+1):
        main.append(main[q])
        q-=1 
    i+=1
for g in range(0,n):
    print(main[g])