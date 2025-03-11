m=10
n=9
lis=[]
mlis=[]
i=1
j=1
while i<=n:
    j=1
    lis=[]
    while j<=m:
        if i==1 or i==9:
            lis.append(1)
        elif i==2 or i==8:
            if j==1 or j==10:
                lis.append(1)
            else:
                lis.append(2)
        elif i==3 or i==7:
            if j==1 or j==10:
                lis.append(1)
            elif j==2 or j==9:
                lis.append(2)
            else:
                lis.append(3)
        elif i==4 or i==6:
            if j==1 or j==10:
                lis.append(1)
            elif j==2 or j==9:
                lis.append(2)
            elif j==3 or j==8:
                lis.append(3)
            else:
                lis.append(4)
        else:
            if j==1 or j==10:
                lis.append(1)
            elif j==2 or j==9:
                lis.append(2)
            elif j==3 or j==8:
                lis.append(3)
            elif j==4 or j==7:
                lis.append(4)
            else:
                lis.append(5)
        j+=1
    print(lis)
    i+=1

l=10//2
print(l)