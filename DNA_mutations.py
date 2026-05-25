import random
import functions

#PROJECT: DNA mutations
data = ["T", "G", "C", "A", "G"]

num = random.randint(1, 3)
length = len(data)

# Weights biased to the end
weight = [3 if i == 0 or i == length - 1 else 1 for i in range(length)]

# Randomly mutates bases in DNA sequence
for mutation in range(num):
    base_position = random.choices(range(length), weight)[0]
    current_base = data[base_position]
    new_base = functions.get_random_base(current_base)
    data[base_position - 1] = new_base


print("".join(data))

