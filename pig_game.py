import random

def roll():
    roll_value = random.randint(1,6)
    return roll_value

print("Welcome to PIG Game!")

while True:
    players = input("Enter number of players (2-4) want to play the game : ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Players must be between 2 and 4.")
    else:
        print("Invalid number. Try again.")

players_score = [0 for i in range(players)]

while True:
    max_score = input("Please enter the max score : ")

    if max_score.isdigit():
        max_score = int(max_score)
        if max_score > 10:
            break
        else:
            print("Max score should be greater than 10.")
    else:
        print("Invalid number. Try again.")

while max(players_score) < max_score:
    for player_no in range(players):

        print(f"\nPlayer no {player_no + 1} 's turn has started!")
        print(f"Current score : {players_score[player_no]}\n")

        current_round_score = 0

        while True:
            rolling = input("Would you like to roll the dice ? (Enter 'y' to continue or any key to quit) : ").lower()
            if rolling != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_round_score = 0
                break
            else:
                print(f"You rolled a {value}")
                current_round_score += value

            print(f"Your score : {current_round_score}")
        
        players_score[player_no] += current_round_score
        print(f"Current score : {players_score[player_no]}\n")

max_score = max(players_score)
winning_player = players_score.index(max_score)

print(f"Player {winning_player + 1} is the winner of the game with a score of {max_score}.")
print("\nThank you for playing PIG Game!")