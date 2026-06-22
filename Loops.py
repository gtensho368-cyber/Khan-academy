
import random

# MODULE IMPORTS:

# Rolls a six sided dice.
dice = random.randint(1, 6)
print(f"You rolled a {dice}")

# Probalistic coin flipping
coin = random.randint(1, 2)
if coin == 1:
    coin = "head"
else:
    coin = "tail"
print(f"You got {coin}")

# Unequal probalities
rate = random.randint(1,10)

if rate == 1 or rate == 2:
    print("You win")
elif rate == 6 or rate == 7:
    print("You lose")
else:
    print("It's a tie")



















