import random
 
'''
1 for snake
-1 for water
0 for gun 
'''

computer = random.choice([-1,1,0])
youstr=input("Enter your choice:")
yourdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}
you=yourdict[youstr]

print(f"Your choice is {reversedict[you]}\n computer choice ({reversedict[computer]})")

if computer==you:
    print("Draw")

else:
    '''if (computer==-1 and you==1): (computer - you)=-2
        print("you win")

    elif(computer==-1 and you==0): (computer - you)=-1
        print("you lose")
    
    elif(computer==1 and you==-1): (computer - you)=2
        print("you lose")

    elif(computer==1 and you==0): (computer - you)=1
        print("you win")

    elif(computer==0 and you==1): (computer - you)=1
        print("you lose")

    elif(computer==0 and you==-1): (computer - you)=-1
        print("you win")
    else:
        print("something went wrong!")
'''

if((computer - you) == -1 or (computer - you)==2):
    print("you lose")
else:
    print("you win")
