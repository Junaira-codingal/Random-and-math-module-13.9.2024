print("\033c")

import random

options = ["Rock", "Paper","Scissors"]

user_choice = input("Choose Rock, Paper,or Scissors: ")

computer_choice = random.choice(options)

print(f"You choose:{user_choice}")
print(f"Computer choose:{computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock samshes scissors! You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock! You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cut Paper! You win!")
else:
    print("You lose!.")