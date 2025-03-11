a=int(input("number of words you want to inter-->"))
lis=[]
i=0
while i<a:
    b=input(f"inter {i} number-->")
    lis.append(b)
    i+=1
print(lis)
p=0
d=""
l2=[]
i=0
while i<a:
    d=lis[i]
    if lis[i] in l2:
        i+=1
        continue
    print(d,"repeat",lis.count(d),"time")
    l2.append(d)
    p+=1
    i+=1
print(f"this list has {p} unique worlds")