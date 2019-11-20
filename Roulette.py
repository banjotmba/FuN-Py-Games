
import random

creditscore = 100   ##starting credit

print("You can choose 'Odd' or 'Even'. You have a starting credit of $%s." %creditscore)
print("-")

while creditscore > 0:
    print("Credit Balance: %s" %creditscore)
    print()
    bet=input("Even or Odd: ")
    betamount=abs(int(input("How much would you like to bet for %s?: " %bet)))
    
    while betamount>creditscore:
        print("You don't have enough credit.")
        betamount=abs(int(input("How much would you like to bet for %s?: " %bet)))
    roll=random.randint(1,2)
    
    if bet=="Odd" and roll==1 or bet=="Even" and roll==1:
        creditscore-=betamount
        
        if bet=="Odd" and roll==2 or bet=="Even" and roll==2:
            creditscore+=betamount
        else:
            print()
    
    
    if creditscore <= 0:
        print("You Lose! Your credit score has reached 0 or below.")
        print("Your Credit Balance: %s" %creditscore)
        input("Restart?")
        print()
        creditscore=100
