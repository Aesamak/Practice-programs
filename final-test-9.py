def rw(st):
    print("",st)
    i=0
    ts=""
    fs=""
    while i<len(st):
        ts+=st[i]
        if st[i]==" " or i==len(st)-1:
            if i==len(st)-1:
                fs+=" "+ts[::-1]
            else:
                fs+=ts[::-1]
            ts=""
        i+=1
    print(fs)
st="Dream big work hard stay humble"
rw(st)

    