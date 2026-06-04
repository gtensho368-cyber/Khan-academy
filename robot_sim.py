
import random
import functions

grid = 15
pos = random.randint(1, grid)
direct = "Right"

# robot picks random action
for i in range(4):
    action = random.randint(1, 2)
    if action == 1:
        pos = functions.move_robot_forward(pos, direct, grid)
    else:
        direct = functions.reverse_direction(direct)

    functions.draw_movement(pos, direct, grid)












