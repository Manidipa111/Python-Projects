print("Welcome to FLAMES Game!\n")

player1 = input("Player 1 : ").lower()
player2 = input("Player 2 : ").lower()

for i in set(player1+player2):
    cnt1 = player1.count(i)
    cnt2 = player2.count(i)

    count = min(cnt1,cnt2)

    player1 = player1.replace(i, "", count)
    player2 = player2.replace(i, "", count)

str_len = len(player1+player2)

result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

while len(result) > 1:

    split_index = (str_len % len(result) -1)

    if split_index >= 0:
        left = result[ : split_index]
        right = result[split_index+1 : ]

        result = left + right

    else:
        result = result[ : len(result)-1]
    
print(f"\nRelationship status : {result[0]}")

print("\nThank you for playing FLAMES Game!")