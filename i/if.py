a = int(input("Enter your age:"))

if (a>=18):
    print("You are eligiable to vote!")

elif (a<0):
    print("invalid age")
elif (a==0):
    print("you are enter 0 which is invalid age")
else:
    print("You are not eligible to vote.")