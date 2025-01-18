'''def avg():

    a =int(input("Enter the number:"))
    b = int(input("Enter the number:"))
    c = int(input("Enter the number :"))

    average = (a+b+c)/3
    print("the average of three numbers is :",average)

avg()
'''

'''def gd(name,ending):
    print("Good day"+name)
    print(ending)
gd("Aman","Have a nice day")'''

'''def gd(name,ending):
    print("Good day"+name)
    print(ending)
    return "done"

a = gd("Aman","Have a nice day")
print(a)'''

# default argument

def gd(name,ending="Have a nice day"):
    print(f"Good day {name}")
    print(ending)

gd("Aman")