
import functions
import random

""" Playing a game of rock, paper scissors """
     
for i in range(3):
    me = functions.player(input("Enter(rock, paper or scissors): "))
    comp = functions.comp_choice()

    if me == comp:
        print("It's a tie")
        continue

    if functions.win(comp, me):
        print("Bad")
    else:
        print("Good")










