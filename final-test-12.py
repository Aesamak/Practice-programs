dis={}
str="4of Fo1r pe6ople g3ood th5e the2"
a=str.split(" ")
j=0
while j<len(a):
    c=a[j]
    i=0
    while i<len(c):
        try:
            n=int(c[i])
            num=c[i]
        except ValueError:
            pass
        i+=1
    j+=1
    dis.update({f"{num}":f"{c}"})
x=1
while x<=len(a):
    na=" ".join(dis[key] for key in sorted(dis.keys()))
    x+=1
print(na)