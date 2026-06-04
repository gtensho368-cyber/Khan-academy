
import random
"""WERE I PUT ALL MY PROJECTS FUNCTIONS"""

# DNA mutation project functions
""" Generates the nucleiotide bases for a DNA sequence """
def get_random_base(base):
    purines = ["A", "G"]
    pyrimides = ["C", "T"]

    if base in purines:
        choices = [b for b in purines if b != base]
    else:
        choices = [b for b in pyrimides if b != base]

    return random.choice(choices)

# Avatar generator 
""" Generates features for a avatar. """
def nose(num):
    if num == 1:
        print("   >") 
    elif num == 2:
        print("   @")
    else: 
        raise ValueError("non valid nose")
    
def ear(num):
    """ Generates the character hairline"""
    if num == 1:
        print(" -----")
    elif num == 2:
        print(" /-\\_/-\\")
    else:
        raise ValueError("non valid scalp")
    
def eyes(num):
    if num == 1:
        print("  0 - 0 ")
    elif num == 2:
        print("  ö . ö ")
    else:
        raise ValueError("non valid scalp")
    
def mouth(num):
    if num == 1:
        print(" -----")
    elif num == 2:
        print(" (||||)")
    else:
        raise ValueError("non valid mouth")

# Longest name 
def find_longest_name(names):
    longest = "" 
    for name in names:
        if len(name) > len(longest):
            longest = name
    return print(f"Longest name is {longest}")

# Screen time
""" Returns minutes spent """
def minutes_spent(apps, excluded):
    mins = 0
    for min in apps:
        if min == "" or min in excluded:
            continue
        mins += 1
        
    return mins

""" Returns the amount of sessions taken """
def sessions_taken(data):
    num = 0
    previous = ""
    for min in data:
        if min != "" and previous == "":
            num += 1
        previous = min
    return num

""" Getting averages """
def screen_time_average(time, session):
    if session == 0:
        return 0
    
    return round(time/session, 1)

# Nim stone game
""" Gives the computer choice """
def computer_choice(stones):
    if stones == 1:
        return 1
    elif stones >= 2:
        return random.randint(1, 2)

""" Player choice valid inclusion """
def player_choice():
    removed = 0
    if removed != 1 or removed != 2:
        removed = int(input("Pick a number of stones(1-2): "))
    return removed

def visualize(stones):
    show = "O " * stones 
    state = f"({stones} stones)"
    return show + state


""" Returns player's starting point """
def initialize():
    return random.randint(10, 16)


# Rock Paper Scissors game
""" Validates player's choice """
def player_choice(): 
    valid = ("Rock", "Paper", "Scissors")
    answer = input("Pick Rock, Paper or Scissors: ")

    while answer not in valid:
        answer = input("Retry: ")
    return answer

def computer_choice():
    """ Picks the computer choice evenly """
    comp = random.randint(1, 3)
    if comp == 3:
        return "Scissors"
    elif comp == 2:
        return "Paper"
    else:
        return "Rock"

def win_format(comp, user):
    """ Determine win format by returning a boolean value """
    if user == "Rock" and comp == "Scissors":
        return True
    elif user == "Scissors" and comp == "Paper":
        return True
    elif user == "Paper" and comp == "Rock":
        return True
    else:
        return False

def score_format(comp, user):
    """ Returns the scores of bote sides """
    return print(f"Score>> {user}(you) - {comp}")

# Robot simulator
""" Reverses direction """
def reverse_direction(direct):
    if direct == "Left":
        return "Right"
    else:
        return "Left"

""" Gives the direction a symbol to represent the robot """
def get_direction_symbol(direct):
    if direct == "Left":
        return "<"
    else:
        return ">"

""" Makes the drawing based on grid """
def draw_movement(pos, direct, grid_size):
    grid = "|"
    for space in range(grid_size):
        if space == pos - 1:
            robot = get_direction_symbol(direct)
            grid = grid + " " + robot + " "
        else:
            grid = grid + " . "

    print(grid + "|") 

""" Moves the robot forward, except when it's at the end """
def move_robot_forward(pos, direction, grid_line):
    if direction == "Left":
        return max(1, pos - 1)
    else:
        return min(pos + 1, grid_line)














