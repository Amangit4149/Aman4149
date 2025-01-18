marks1=int(input("Enter your marks 1:"))
marks2=int(input("Enter your marks 2:"))
marks3=int(input("Enter your marks 3:"))

total_parcentage=(100)*(marks1+marks2+marks3)/300

if (total_parcentage>=40):
    print("You are passed",total_parcentage)
else:
    print("You are fail ,better luck next time",total_parcentage)