import random
import time

OPERATORS = ["+","-","*","/"]
MIN_OPERAND = 2
MAX_OPERAND_AS = 99 # Max operand for addition and substraction
MAX_OPERAND_L = 100 # Left Max operand for Multiplication and Division
MAX_OPERAND_R = 10 # Right Max operand for Multiplication and Division
TOTAL_PROB = 10

def generate_prob():
    operator = random.choice(OPERATORS)

    if operator == "/":
        while True:
            left = random.randint(MIN_OPERAND,MAX_OPERAND_L)
            right = random.randint(MIN_OPERAND,MAX_OPERAND_R)
            if(left%right == 0):
                break

    elif operator == "*":
        left = random.randint(MIN_OPERAND,MAX_OPERAND_L)
        right = random.randint(MIN_OPERAND,MAX_OPERAND_R)

    elif operator == "-":
        while True:
            left = random.randint(MIN_OPERAND,MAX_OPERAND_L)
            right = random.randint(MIN_OPERAND,MAX_OPERAND_R)
            if(left >= right):
                break
            
    else:
        left = random.randint(MIN_OPERAND,MAX_OPERAND_AS)
        right = random.randint(MIN_OPERAND,MAX_OPERAND_AS)

    exp = str(left)+" "+operator+" "+str(right)

    return exp

input("Press enter to start!")

start_time = time.time()

for i in range(TOTAL_PROB):
    prob = generate_prob()
    ans = round(eval(prob))

    while True:
        user_ans = input(f"\nProblem #{i+1} : {prob} = ")

        if user_ans == str(ans):
            break
        else:
            print("Wrong Answer! Try again.")

end_time = time.time()

tot_time = round((end_time - start_time))

if(tot_time < 60):
    sec = tot_time
    print(f"\nCongratulations! You have completed the challenge in {sec} secs.\n")
else:
    min = round(tot_time // 60)
    sec = tot_time % 60
    print(f"\nCongratulations! You have completed the challenge in {min} min {sec} secs.\n")