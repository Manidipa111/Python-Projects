import random

print("Welcome to Mastermind Game!")

number = random.randint(1000,9999) #Generating a 4 digit random number

def user_guess():
    while True:
        num = input("\nGuess a 4 digit number : ")
        if num.isdigit():
            num = int(num)
            if 1000 <= num <= 9999:
                return num
            else:
                print("This is no a 4 digit number. Try again.")
        else:
            print("Invalid number. Try again.")

guessed_number = user_guess()

if number == guessed_number:
    print("\nGreat! You guessed the number in just 1 try! You're a Mastermind!\n")
else:
    guess_count = 0

    while True:
        guess_count += 1
        correct = ['X']*4
        count = 0
        number = int(number)

        if (number == guessed_number):
            print(f"\nYou've become a Mastermind. \nIt took you only {guess_count} tries. \nThe correct number is {number}.\n")
            break
        else:
            number = str(number)
            guessed_number = str(guessed_number)

            for i in range(0,4):
                if (number[i] == guessed_number[i]):
                    correct[i] = number[i]
                    count += 1
            
            if count != 0:
                print(f"Not quite the number. But you did get {count} digit(s) correct!")
                print("Also these numbers in your input were correct.")
                for i in correct:
                    print(i,end=" ")
                print()

            elif count == 0:
                print("None of the numbers in your input match. \nTry again!")
        
        guessed_number = user_guess()

print("Thank you for playing Mastermind Game!")