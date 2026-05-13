
# learning unit tests with boolean values
def bread(flour, eggs):
    """ Returns True if flour and eggs are enough to make bread"""
    return flour >= 3 and eggs >= 2

bread = (bread(4, 4))
print("Gregor is makinng bread right? ", bread)

# learning with Number values
def speed(gas, distance):
    """" Returns values based on gas to distance"""
    if gas < distance:
        return 0
    elif gas >= distance * 2:
        return 2
    else:
        return gas / distance
    
speed = speed(11, 5)

print("Speed is covered " + str(speed) + "x")

