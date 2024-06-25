import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock/paper/scissors): ").lower()
    while user not in choices:
        user = input("Invalid input. Enter your choice (rock/paper/scissors): ").lower()

    print(f"\nComputer chose {computer}, you chose {user}.\n")

    if user == computer:
        return "It's a tie!"
    if user == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    if user == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    if user == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

print(play_game())
