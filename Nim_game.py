
import random
import functions

stones = functions.initialize()
player = True

print("Pick from one to two stones\n")

# Taking turns
while stones > 0:
    print(functions.visualize(stones))
    stone = functions.visualize(stones)
    if player:
        comp = functions.player_choice()
    else:
        comp = functions.computer_choice(stones)
        print(f"computer picked {comp} stones")
    

    stones -= comp
    player = not player

# previous player loses
if player:
    print("You lost.")
else:
    print("Computer lost.")








