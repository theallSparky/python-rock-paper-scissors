import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Please type Rock/Paper/Scissors... or 'Q' to quit: ").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0   paper: 1    scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win this round!")
        user_wins+=1
    elif user_input == "rock" and computer_pick == "rock":
        print("Draw this round!")
    elif user_input == "paper" and computer_pick == "rock":
        print("You win this round!")
        user_wins+=1
    elif user_input == "paper" and computer_pick == "paper":
        print("Draw this round!")
    elif user_input == "scissors" and computer_pick == "papers":
        print("You win this round!")
        user_wins+=1
    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw this round!")
    else:
        print("You lost!")
        computer_wins +=1

print(f"You won {user_wins} number of times and the computer won {computer_wins} number of times!")
print("Goodbye, thank you playing!")