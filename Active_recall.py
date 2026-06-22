
import random
import functions

""" Where I actively recall code: I delete them when done"""



""" Screen time """

""" Murim skill combination sequence """
def get_random_base(base):
    for i in len(base) - 1:
        if "Dragon" in i:
            base[i] = "Might"
    return base

bases = ["Dragon mist", "Tiger fist", "Blossom blade"]
print(get_random_base(bases))




















