import random
con=True
print("Let's play Rock Paper Scissors")
while con:
    n=random.randint(1,3)
    cho=input("choose Rock(r), Paper(p) or Scissors(s)--->")
    cho=cho.lower()
    lis=["r","p","s"]
    dic={
        "r": 1,
        "p":2,
        "s":3
    }
    dicc={
        1:"r",
        2:"p",
        3:"s"
    }
    if cho in lis:
        if dic[cho]==n:
            print(f"Draw, you chose {cho} or computer chose {dicc[n]}")
        elif dic[cho]==1:
            if n==2:
                print(f"you lose, you chose {cho} or computer chose {dicc[n]}")
            else:
                print(f"you win, you chose {cho} or computer chose {dicc[n]}")
        elif dic[cho]==2:
            if n==3:
                print(f"you lose, you chose {cho} or computer chose {dicc[n]}")
            else:
                print(f"you win, you chose {cho} or computer chose {dicc[n]}")
        elif dic[cho]==3:
            if n==1:
                print(f"you lose, you chose {cho} or computer chose {dicc[n]}")
            else:
                print(f"you win, you chose {cho} or computer chose {dicc[n]}")
        pa=input("play again (y/n)--->")
        pa=pa.lower()
        if pa=="y":
            con=True
        else:
            con=False
    else:
        print("envalid entry only enter r,p and s")