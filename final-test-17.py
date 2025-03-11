n=int(input("A positive integer(the number itself) :"))
p=int(input( "A positive integer (the power to which the digits will be raised) :"))
sn=str(n)
s=0
for i in sn:
    i=int(i)
    pp=i**p
    p+=1
    s+=pp
print(f"s={s}")
# find k so s=k*n then k=s/n
k=s/n
if k>1:
    print(f"k={int(k)}")
else:
    print("k is not exist")