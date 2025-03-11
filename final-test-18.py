a="(aesam)()"
b="())(()"
d="(())((()())())" 
e="(" 
i=0
c=0
o=0
n=b
if n[0]=="(":
    while i< len(n): 
        if n[i]=="(":
            o+=1
        elif n[i]==")"and n[i-1]=="(":
            c+=1
        i+=1
    if o==c:
       print("true entry") 
    else:
        print("false entry")  
elif n[0]==")":
    print("false entry")
    