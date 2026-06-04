
import functions
import random

""" Playing a game of rock, paper scissors """
user_score = 0
comp_score = 0

# First to reach two points wins 
while user_score < 2 and comp_score < 2:
    user = functions.player_choice()
    comp = functions.computer_choice()
    print(f"Computer chose {comp}.")

    if user == comp:
        print("It's a tie")
        continue

    if functions.win_format(comp, user):
        print("You win")
        user_score += 1
    else:
        comp_score += 1 
    
    functions.score_format(comp_score, user_score)

if user_score > comp_score:
    print("The murim is proud of you")
else:
    print("You need more training")


























