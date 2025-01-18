'''n=int(input("Enter a number:"))

product = 1
for i in range(1,n+1):
    product=product*i

print(f"the factorial of{n} is {product}")
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    
    return n*factorial(n-1)
n=int(input("Enter a number:"))
print(f"The factorial of this number is:{factorial(n)}")
