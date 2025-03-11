def cal_sc(sl):
    w=0
    l=0
    d=0
    p=0
    for i in sl:
        # print(i)
        x,y=i.split(":")
        x=int(x)
        y=int(y)
        if x > y:
            w+=1
            p+=3
            #3 point
        elif x < y:
            l+=1
            #0 point
        else :
            d+=1
            p+=1
            # 1 point
    print(f"total no of match win is {w}\ntotal no of match draw is {d}\ntotal no of match lose is {l}")
    return p

sl=["3:2","4:5","2:1","6:7","3:3","5:6","2:2","2:3","1:0"]
a=cal_sc(sl)
print(f"total number of points got in the championship {a}")