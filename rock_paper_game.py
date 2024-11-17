import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice, please select rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
if __name__ == "__main__":
    play_rps()