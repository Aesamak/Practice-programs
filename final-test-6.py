import array
a=array.array('i',[1,-2,4,10])
print(a)
i=0
s=0
print("sum of",end=" ")
while i<len(a):
    while i<len(a) and a[i]>=0 :
         print(a[i],end=" ")
         s+=a[i]
         i+=1
    i+=1
   
print("=",s)