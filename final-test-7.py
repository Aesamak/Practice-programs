import array
a=array.array('i',[2,1,5,8,4,10])
print(a)
a_list = sorted(a)
print(a_list)
sum=0
for i in  a_list[1:5]:
    sum+=i
print(sum)