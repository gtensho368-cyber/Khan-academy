
# stimulating the fictional population of "Viltrumites"

import random

# Starting population
population = 10000

# internal purge and plague stimulation
for year in range(2):
    # internal purge: 10% survive
    population = population // 10
    # plague: random number of deaths up to half the population
    plague = random.randint(0, population // 2)
    population -= plague
    print(f"Year {year + 1}: Population is {population} after purge and plague.")

# conquest stimulation
for year in range(2, 5):
    # conquest: random number of deaths up to 30% of the population
    conquest = random.randint(0, population * 3 // 10)
    population -= conquest
    print(f"Year {year + 1}: Population is {population} after conquest.")

print(f"Final population after 5 years: {population}")