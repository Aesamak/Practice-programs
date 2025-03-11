strarr = ["a", "bbbbb", "ccc", "dddd","kkkkk"]
epl=[]
k=3
long_str=""
if k>len(strarr) or k==0 :
    print(f"It's not possible to take {k} consecutive strings")
else:
    i=0
    l=0
    while i<len(strarr):
        j=0
        new=""
        while j<k:
            if l<len(strarr):
                new+=strarr[l]
                co=True
                l+=1
                j+=1
            else:
                new=""
                co=False
                break
        if co==True:
            epl.append(new)
        l-=(k-1)
        i+=1
    long_str = max(epl, key=len)
    print(epl)  
    print(long_str,"is longer string")
