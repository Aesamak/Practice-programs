a=input("enter a string--->")
lis=[]
i=0
j=0
l2=[]
while i<len(a):
    current=a[i]
    coun=0
    while j<len(a):
        if current == a[j]:
            coun+=1
            j+=1
        else: 
            break
        i+=1
    lis.append(current)
    
print(lis)

