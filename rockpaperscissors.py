from random import choices, randint
choices = ["rock" , "paper" , "scissor"]
computer = choices[randint(0,2)]

print("Welcome to the Rock , Paper , Scissors Game!\n")
player = input("Your choice: ").lower()
print("computer chooses: ", computer)

if player == computer:
    print("DRAW!")
elif player == "rock" and computer == "paper":
    print("Computer Wins!")
elif player == "rock" and computer == "scissors":
    print("Player Wins!")
elif player == "paper" and computer == "scissors":
    print("Computer Wins!")
elif player == "paper" and computer == "rock":
    print("Player Wins!")
elif player == "scissors" and computer == "rock":
    print("Computer Wins!")
elif player == "scissors" and computer == "paper":
    print("player Wins!")

