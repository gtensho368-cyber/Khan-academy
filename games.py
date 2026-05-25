
# This is where I code all my games
from time import time

import functions

# football match simulator


 # Creating a murim themed game 
print("         ")
jin = functions.technique_rank("Jin") 
won = functions.technique_rank("Won")

choice = ""
while choice not in ["Jin", "Won"]:
    choice = input("Pick a fighter between Jin and Won: ")
    if choice == "Jin":
        print("You picked Jin")
        opp = won
        player = jin
        print(f"{jin} and {won}")
    elif choice == "Won":
        print("You picked Won")
        opp = jin
        player = won
        print(f"Jin is {jin} and Won is {won}")
    else: 
        print("You chose wrong. Pick again.")




     