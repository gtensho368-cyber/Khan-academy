
import random

# LIST INDICES
data = [1, 2, 3, 4, 5, 6]

# Negative indices
print(data[-1])

print(len(data) - 1)

data[-1] = 6
print(data)

data[-1] = data[-1] - 1
print(data)

# Positive indices
print(data[1])
