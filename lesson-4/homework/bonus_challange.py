
#Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.

#The computer randomly chooses rock, paper, or scissors using random.choice().
#The player enters their choice.
#Display the winner and keep track of scores for the player and the computer.
#First to 5 points wins the match.

import random

player_score = 0
computer_score = 0

random_choice = random.choice(["rock", "paper", "scissors"])

while player_score < 5 and computer_score < 5:
    player_choice = input("Please, enter your choice ('rock', 'paper', 'scissors') : ")
    if player_choice == random_choice:
        print("It's a tie!")
        random_choice = random.choice(["rock", "paper", "scissors"])
    elif player_choice == "rock" and random_choice == "scissors":
        print("You win!")
        player_score += 1
        random_choice = random.choice(["rock", "paper", "scissors"])
    elif player_choice == "rock" and random_choice == "paper":
        print("Computer wins!")
        computer_score += 1
        random_choice = random.choice(["rock", "paper", "scissors"])
    elif player_choice == "scissors" and random_choice == "rock":
        print("Computer wins!")
        computer_score += 1
        random_choice = random.choice(["rock", "paper", "scissors"])
    elif player_choice == "scissors" and random_choice == "paper":
        print("You win!")
        player_score += 1
        random_choice = random.choice(["rock", "paper", "scissors"])
    elif player_choice == "paper" and random_choice == "rock":
        print("You win!")
        player_score += 1
        random_choice = random.choice(["rock", "paper", "scissors"])
    elif player_choice == "paper" and random_choice == "scissors":
        print("Computer wins!")
        computer_score += 1
        random_choice = random.choice(["rock", "paper", "scissors"])
    else:
        print("Invalid choice. Please, enter rock, paper or scissors.")
        random_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Player: {player_score} Computer: {computer_score}")

if player_score == 5:
    print("You win the match!")
else:
    print("Computer wins the match!")