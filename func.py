
import random
# I don't want to create multiple files for diffrent projects, so i'm putting all my functions here.

# Module for functions of a football game

for minutes in range(90):
    def home_goal(time):
        """Generate the goals possibility within time intervals."""
        if time <= 50:
            return random.randint(0, 1)
        elif time <= 90 and time > 50:
            return random.randint(0, 4)



    def away_goal(time):
        """Generate the goals possibility of the opposing team within time intervals."""
        if time <= 50:
            return random.randint(0, 1)
        elif time <= 90 and time > 50:
            return random.randint(0, 4)


# Module for functions of a murim themed game

def technique():
    """Randomly generates techniques numbers"""
    num = random.randint(1, 200)
    if num < 100:
        rank = "Master"
    else:
        rank = "Elite"
    
    return rank