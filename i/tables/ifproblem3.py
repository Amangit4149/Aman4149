p1="Make a lot of money"
p2="Buy now"
p3="subscribe now"
p4="click here"

massage = input("Enter your massage:")

if ((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("Spam massage")
else:
    print("Not a spam massage")
    