
""" Determines the winner of a murim themed clash """
import random
import functions

MC = 0 
SC = 0

for i in range(3):
    # Determines winner based on move 
    MC = functions.arts_combat()
    SC = functions.arts_combat()
    
    if MC == SC:
        print("Masters of equal caliber")
    elif MC == "Moon blade" and SC != "Moon blade":
        print("The vagabond won somehow")
        break
    else:
        print("Someone's regressing.")
        break



















