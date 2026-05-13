
import random
# I don't want to create multiple files for diffrent projects, so i'm putting all my functions here.

# Module for functions of a football game



# Module for functions of a murim themed game

def technique():
    """Randomly generates techniques numbers"""
    num = random.randint(1, 200)
    if num < 100:
        rank = "a Master"
    else:
        rank = "an Elite"
    
    return rank