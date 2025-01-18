

'''x=input("enter the opration (F/C):").upper()
temp=float(input("enter temp:"))
if x=="C":
    temp=((temp*9)/5)+32
    print(f"The temperature in Fahrenheit is:{temp}")
elif x=="F":
    temp=((temp-32)*5/9)
    print(f"The temperature in celsius is : {temp}")
'''
def f_to_c(f):
    return (f-32)*5/9

f = int(input("Enter temperature in F:"))
c=f_to_c(f)
print(f"{round(c,2)}")