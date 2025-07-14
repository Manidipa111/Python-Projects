import random

print("Welcome to \'ROCK PAPER SCISSORS Game\'.")

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("\nType Rock/Paper/Scissors or Q to quit : ").lower()

    if user_choice == "q":
        break
    elif user_choice not in options:
        print("Type a correct choice.")
        continue

    computer_choice = random.choice(options)

    print(f"Your choice {user_choice}.")
    print(f"Computer choice {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a Tie.")

    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win.")
        user_wins += 1

    elif user_choice == "paper" and computer_choice == "rock":
        print("You win.")
        user_wins += 1

    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win.")
        user_wins += 1

    else:
        print("Computer win.")
        computer_wins += 1


print(f"\nYou won {user_wins} times.")
print(f"The Computer won {computer_wins} times.")
print("Thank you for Playing \'ROCK PAPER SCISSORS Game\'.")