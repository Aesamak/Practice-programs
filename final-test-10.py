wo=input("enter the word: ")
m=int(len(wo)/2)
print(m)
if len(wo)%2==0:
    print(f"{wo[(m-1)]}{wo[(-m)]}")
else:
    print(wo[m])
