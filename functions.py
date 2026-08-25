
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
        raise ValueError("non valid ear")
    
def eyes(num):
    if num == 1:
        print("  0 - 0 ")
    elif num == 2:
        print("  ö . ö ")
    else:
        raise ValueError("non valid eyes")
    
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
def comp_choice():
    """ Generate random choice """
    option = random.randint(1, 3)
    if option == 1:
        return "rock"
    elif option == 2:
        return "paper"
    else:
        return "scissors"
    
def player(play):
        """ Validates user input """
        game = ["rock", "paper", "scissors"]
        if play.lower() in game:
            play = play.lower()
        else:
             play = input("Retry: ")
        return play

def win(comp, player):
     if comp == "rock" and player == "scissors":
          return True
     elif comp == "scissors" and player == "paper":
          return True
     elif comp == "paper" and player == "rock":
          return True
     else:
          return False

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


# Murim combat simulator 
""" Determines the combat move """
def arts_combat():
    art_1 = "Tiger fist"
    art_2 = "Moon blade"
    
    chose = random.randint(1, 2)
    if chose == 1:
        return art_1
    else:
        return art_2

# Encrypting a message
def encryption(message, key):
    """ Returns the encrytion of a message """
    result = ""
    
    for char in message: 
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = (ord(char) - base + key) % 26
            result += (chr(base + shift))
        else: 
            result += char 

    return result


























