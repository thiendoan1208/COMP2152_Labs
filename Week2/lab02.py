# rock, paper, scissors game
import random

def rps_game():
    try:
        choice = ["rock", "paper", "scissor"]
        player_choice = int((input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")))
        computer_choice = random.randrange(1, len(choice) + 1)

        if player_choice < 1 or player_choice > 3:
            print("Error: Choice must be between 1 and 3.")
            return
        else :
            print(f"Your choice is {choice[player_choice - 1]}")
            print(f"Computer choice is {choice[computer_choice - 1]}")

        if player_choice == 1 and computer_choice == 3:
            print("Rock beats Scissors - You win!")
        elif player_choice == 2 and computer_choice == 1:
            print("Paper beats Rock - You win!")
        elif player_choice == 3 and computer_choice == 2:
            print("Scissors beats Paper - You win!")
        elif player_choice == computer_choice:
            print("It's a tie")
        else:
            print("You lose!")
    except ValueError:
        print("Error: Input must be a integer.")

rps_game()