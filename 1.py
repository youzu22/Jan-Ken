wins = 0
losses = 0
draws = 0
print("🎮 Welcome！🎮")
print("RULE：1 = 🪨 Rock，2 = ✂️ Scissors，3 = 🧻 Paper")

# Define choices
choices = {1: "Rock🪨", 2: "Scissors✂️", 3: "Paper🧻"}

import random
# Computer's random choice
a = random.randint(1, 3)

# User's input
x = int(input("Enter your choice (1: Rock, 2: Scissors, 3: Paper): "))

# Validate input
if (x > 3) or (x < 1):
    print("Invalid input")
else:
    print(f"You chose: {choices[x]}\nComputer chose: {choices[a]}")

    # Determine the result
    if x == a:
        print("It's a tie!")
    elif (x == 1 and a == 2) or (x == 2 and a == 3) or (x == 3 and a == 1):
        print("🙂🙂🙂🙂🙂")
        print("You win!")
        print("✨✨✨✨✨")
    else:
        print("😃😃😃😃😃")
        print("You lose!")
        print("🃏🃏🃏🃏🃏")