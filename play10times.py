#no. of play 10 times 
#result : who win how many , draw how many 
#q to quit

import random
userWins = 0
compWins = 0
draws=0
chance=0
options = ["rock" , "paper", "scissors"]
while chance<10:
    chance += 1
    userinput = input("Enter your chooice \n Type Rock/Paper/Scissors or Q to quit ").lower()
    if userinput == "q":
        break

    if userinput not in options:
        continue
    
    compchoice = random.choice(options)
    print(" Computer chooses" , compchoice)

    if userinput == compchoice:
        print("It's a DRAW!!")
        draws += 1
    
    elif userinput == "rock" and compchoice=="scissors":
        print("You Win!")
        userWins += 1
    
    elif userinput == "paper" and compchoice=="rock":
        print("You Win!!")
        userWins += 1
    
    elif userinput == "scisssors" and compchoice=="paper":
        print("You Win!!")
        userWins += 1    
    
    else:
        print("You loose!")
        compWins += 1

print("You wins ", userWins, "times")
print("Computer wins ", compWins,"times")
print("Draws = ", draws)
print("Thankyou for playing")