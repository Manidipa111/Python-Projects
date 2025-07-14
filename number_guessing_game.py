import random

print("Welcome to \'Number Guessing Game\'.")

while True:
    game = input("\nDo you want to play \'Number Guessing Game\'? (Y/N) : ").lower()
    if game == 'y':
        max_range = input("Enter maximum range : ")

        if max_range.isdigit():
            max_range = int(max_range)

            if max_range < 0:
                print("Enter a positive number : ")
                quit()
        else:
            print("Please enter a number next time.")
            quit()

        number = random.randint(0,max_range)
        guess = 0

        while True:
            number_guessed = input("Guess a number : ")
            guess += 1

            if number_guessed.isdigit():
                number_guessed = int(number_guessed)
            else:
                print("\nPlease enter a number.")
                continue

            if number_guessed == number:
                print(f"\nCongratulation, you guessed the correct number. \nThe number is {number}. \nNumber of guesses : {guess}")
                break
            elif number_guessed > number:
                print("\nYou guessed a higher number.")
            elif number_guessed < number:
                print("\nYou guessed a lower number.")

    elif game == 'n':
        print("\nThank you for Playing \'Number Guessing Game\'.")
        break

    else:
        print("\nEnter a valid choice.")