def p(a):
        if a<0:
             a=-(a)
        i=1
        divisor=1
        while (a / divisor >= 10):
                divisor *= 10
        
        while divisor>=1:
            num=(a/divisor)%10
            print(int(num))
            divisor/=10

a=int(input("enter positive number-->"))
p(a)

