

print("Now let's stimulate a bee hive")

# Bee hive simulation
needsNectar =  2000
hasNectar = 0
deposits = 0

# Week of hive activity
for hour in range(7*18):
    
    # dropoff of bees depositing nectar
    dropoff = random.randint(hasNectar//4, hasNectar//2)
    deposits = deposits + dropoff
 

    # probability of finding nectar
    pickups = random.randint(needsNectar//4, needsNectar//2)

    hasNectar = pickups + hasNectar + dropoff
    needsNectar = needsNectar - pickups - dropoff

# 90 deposits to make a gram of honey
honey = deposits // 90  
print(f"Total honey produced: {honey} grams")

# let's make an ant hill simulation
print("Now let's stimulate an ant hill")
needsFood = 1000
hasFood = 0
for day in range(30*18):
    # dropoff of ants depositing food
    dropoff = random.randint(hasFood//4, hasFood//2)
    hasFood = hasFood + dropoff
    needsFood = needsFood - dropoff

    # probability of finding food
    pickups = random.randint(needsFood//4, needsFood//2)
    hasFood = pickups + hasFood - dropoff
    needsFood = needsFood - pickups + dropoff

print(f"Total food collected: {hasFood} units")