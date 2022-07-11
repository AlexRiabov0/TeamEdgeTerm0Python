import random

print("Let's play Rock Paper Scissors!")

# Challenge
# Find the bugs below:

while True:
    userInput = input("Do you want to play rock, paper, or scissors?\n").lower()
    computerSelection = random.choice(["rock", "paper", "scissors"])
    print("comp ",computerSelection)

    print(f"You played: {userInput} and the computer played: {computerSelection}")
    if userInput == computerSelection:
        print("It's a tie!")
    elif((userInput == "rock" and computerSelection == "paper") or (userInput == "paper" and computerSelection == "scissors") or (userInput == "scissors" and computerSelection == "rock")):{print("You Lose!")}
    elif((userInput == "paper" and computerSelection == "rock") or (userInput == "scissors" and computerSelection == "paper") or (userInput == "rock" and computerSelection == "scissors")):{print("You Win!")}
    else:{print("error")}
    
