
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
""" Generates features for a avatar """
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
        print(" /-\_/-\\")
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