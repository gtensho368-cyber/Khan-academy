
import random
import functions 

# Making the bodyparts
num = random.randint(1, 2)
mix = random.randint(1, 2)

if mix == 1:
    functions.ear(num)
    functions.eyes(num)
    functions.nose(num)
    functions.mouth(num)
else:
    functions.ear(num)
    functions.eyes(1)
    functions.nose(2)
    functions.mouth(num)






