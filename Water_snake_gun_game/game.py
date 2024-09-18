'''
1 for snake
-1 for water
0 for gun
'''
import random
computer =random.choice([-1,0,1])
youstr=(input("Enter your choice "))
youDict={"snake":1,"water":-1,"guns":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you = youDict[youstr]

print(f"you chose  {reversedict[you]} and computer chose {reversedict[computer]}")

if (computer==-1 and you==1):
    print("You won darling")
elif (computer==-1 and you==0):
    print("You lose baby")
elif (computer==-1 and you==-1):
    print("It's a tie")
elif (computer==1 and you==-1):
    print("You lose darling")
elif (computer==1 and you==0):
    print("You won darling")
elif (computer==1 and you==1):
    print("its a tie darling")
elif (computer==0 and you==-1):
    print("You won darling")
elif (computer==0 and you==1):
    print("You lose darling")
elif (computer==0 and you==-0):
    print("You lose darling")
else:
    print("Something went wrong")
           