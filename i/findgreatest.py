def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>b and c>a):
        return c
    
a=1
b=26
c=5
print(greatest(a,b,c))
