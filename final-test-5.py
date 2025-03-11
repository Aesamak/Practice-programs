def re(a):
    li=["!","@","#","$","%","&","1","2","3","4","5","6","7","8","9","0"]
    i=0
    while i<len(li):
     x=li[i]
     a=a.replace(f"{x}","")
     i+=1
    return a

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
print(grid)

def decode_grid(grid):
    decoded = ''
    
    for col in range(m):
        column_string = ''
        for row in range(n):
            column_string += grid[row][col]
        
       
        for char in column_string:
                decoded += re(char)
                
    return decoded

output = decode_grid(grid)
print(output)